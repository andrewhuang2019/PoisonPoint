from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def loginpage():

    return render_template('loginpage.html')
    
@app.route('/mainpage')
def mainpage():
    return render_template('mainpage.html')

@app.route('/mainpage2')
def mainpage2():
    return render_template('mainpage2.html')

@app.route('/educationpage')
def educationpage():
    return render_template('educationpage.html')

@app.route('/reportpage')
def reportpage():
    return render_template('reportpage.html')

@app.route('/summarypage')
def summarypage():

    return render_template('summarypage.html')

@app.route('/location_summary', methods=["POST"])
def summary():
    query= request.json
    name = query['name']
    id = query['ID']
    location = query['location']['location']
    print(name)
    print(id)
    print(location)
    return 'summary'

@app.route('/food_summary', methods=["POST"])
def food_summary():
    query = request.json
    foods1 = query['foods1']
    foods2 = query['foods2']
    foods3 = query['foods3']
    print(foods1)
    print(foods2)
    print(foods3)
    return 'summary'

@app.route('/time_summary', methods=['POST'])
def time_summary():
    query = request.json
    time = query['time']
    print(time)
    return 'summary'

if __name__ == '__main__':
    app.run(debug=True)
