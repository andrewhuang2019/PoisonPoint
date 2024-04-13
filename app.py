from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('autocomplete_template.html')

@app.route('/process', methods=['POST'])
def receivedata():
    data = request.json
    name = data.get('name')
    ID = data.get('ID')
    location = data.get('location')['location']
    print(name, ID, location)
    return ''

if __name__ == '__main__':
    app.run(debug=True)