from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get():
    return jsonify({"message": "Hello, World!"})


@app.route('/report', methods=['POST'])
def report():
<<<<<<< Updated upstream
    return jsonify({"HI"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
=======
    # Get data from the request
    data = request.get_json()
    
    # Process the data (this is just a placeholder)
    # In a real application, you'd do something with this data
    if data:
        return jsonify({"status": "success", "data": data})
    else:
        return jsonify({"status": "error", "message": "No data provided"}), 400

# Add this code to run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6969)
>>>>>>> Stashed changes
