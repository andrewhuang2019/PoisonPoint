from flask import Flask, request, render_template
from report_handler import ReportHandler
from datetime import datetime
import time

app = Flask(__name__)

rh = ReportHandler()

locations = []
times = []

lat = 38.9717
lng = -95.2353

@app.route('/')
def loginpage():

    return render_template('loginpage.html')
    
@app.route('/mainpage')
def mainpage():
    return render_template('mainpage.html')

@app.route('/mainpage2')
def mainpage2():
    # returns info dict for the top 3 most dangerous restaurants near your lat, lng
    # also returns lists for main causes and weighted_sums for each restaurant
    ids = rh.get_dangerous_ids_near_coords(lat, lng)
    dicts = [rh.google_api.get_info_from_place_id(id) for id in ids]
    causes = [rh.get_commonly_reported_items(id) for id in ids]
    weights = [rh.get_danger_weight(id) for id in ids]
    return render_template('mainpage2.html', dicts=dicts, causes=causes, weights=weights)

@app.route('/educationpage')
def educationpage():
    return render_template('educationpage.html')

# clear existing logs of locations and times
@app.route('/reportpage')
def reportpage():
    clear_lists()
    return render_template('reportpage.html')

def clear_lists():
    locations.clear()
    times.clear()

@app.route('/summarypage')
def summarypage():

    return render_template('summarypage.html')

@app.route('/aboutpage')
def aboutpage():
    return render_template('aboutpage.html')

#has data for a single location name, a single ID, and a single geographical latitute/longitude 
@app.route('/location_summary', methods=["POST"])
def summary():
    query= request.json
    name = query['name']
    id = query['ID']
    location = query['location']['location']

    # append name, id to locations
    loc_tuple = (name, id)
    locations.append(loc_tuple)
    return 'summary'

#has data for all three locations and the foods that the user ate at them
@app.route('/food_summary', methods=["POST"])
def food_summary():
    query = request.json
    foods1 = query['foods1']
    foods2 = query['foods2']
    foods3 = query['foods3']
    
    summaries = [foods1, foods2, foods3]
    update_db(summaries)
    return 'summary'

#has data for a single time (for a single location)
@app.route('/time_summary', methods=['POST'])
def time_summary():
    query = request.json
    time = query['time']
    times.append(time)
    return 'summary'

@app.route('/userlocation', methods=["POST"])
def userloc():
    query = request.json
    return render_template('mainpage.html', data=query)

# should be called when food_summary() is called
# makes report objects based on all user information
# only append if there is a summary available
def update_db(summaries):
    items = ["fish","lettuce","chicken","beef","eggs",
            "shellfish","milk","flour","wasabi"]
    for i, food_summary in enumerate(summaries):
        if(food_summary):
            restr_name = locations[i][0]

            place_id = locations[i][1]

            raw_time = times[i]
            raw_time = raw_time.replace("-", "/")
            eaten_datetime_obj = datetime.strptime(raw_time, '%Y/%m/%d')
            curr_time = datetime.today()
            # datetime - datetime obj = delta_time obj, how convinient!
            delta_time = curr_time - eaten_datetime_obj
            days_elapsed = delta_time.days
            
            time_sec = int(time.time())

            bool_list = []
            for ill_food in items:
                bool_list.append(ill_food in food_summary)
            
            items_eaten = str(bool_list)[1:-1]

            # print(f"place_id = {place_id}")
            # print(f"days_elapsed: {days_elapsed}")
            # print(f"time: {time_sec}")
            # print(f"items_eaten: {items_eaten}")
            # print(f"restr_name: {restr_name}")

            rh.add_to_db(place_id, days_elapsed, time_sec, items_eaten, restr_name)
            render_template("/summarypage")

if __name__ == '__main__':
    app.run(debug=True)
