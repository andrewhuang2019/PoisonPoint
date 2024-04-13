
'''
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods =['GET','POST'])
def loginpage():
    if request.method == 'GET':
        
        return render_template('loginpage.html')
    elif request.method == 'POST':
        username = request.form.get("username")
        return mainpage(username)


@app.route('/mainpage')
def mainpage(username):
    print(username)
    return render_template('mainpage.html', username=username)
    
if __name__ == '__main__':
    app.run(debug=True)
    '''
    
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

if __name__ == '__main__':
    app.run(debug=True)
