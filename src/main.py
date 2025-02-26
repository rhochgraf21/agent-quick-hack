from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get():
    return jsonify({"message": "Hello, World!"})

@app.route('/report', methods=['POST'])
def report():
    return jsonify({"HI": "HI"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6969)
