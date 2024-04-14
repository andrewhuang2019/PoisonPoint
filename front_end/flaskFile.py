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

@app.route('/summarypage', methods=["POST"])
def summarypage():
    query= request.json
    name = query['name']
    id = query['ID']
    location = query['location']['location']
    print(name)
    print(id)
    print(location)

    return render_template('summarypage.html')

if __name__ == '__main__':
    app.run(debug=True)
