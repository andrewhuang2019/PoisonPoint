from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receivedata():
    data = request.json  # Assuming JSON data is sent
    # Process the data, here we just print it
    print(data)
    # Respond back with a confirmation or processed result
    return jsonify({"status": "Received", "yourData": data}), 200

if __name__ == '_main':
    app.run(debug=True)