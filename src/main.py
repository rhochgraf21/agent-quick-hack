from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get():
    return jsonify({"HI"})


@app.route('/report', methods=['POST'])
def report():
    return jsonify({"HI"})
