from flask import Flask, request, jsonify, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get():
    form_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Report Form</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .form-group { margin-bottom: 15px; }
            label { display: block; margin-bottom: 5px; }
            input, textarea { width: 100%; padding: 8px; }
            button { padding: 10px 15px; background: #4CAF50; color: white; border: none; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>Submit Report</h1>
        <form action="/report" method="post">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" required></textarea>
            </div>
            <button type="submit">Submit Report</button>
        </form>
    </body>
    </html>
    """
    return Response(form_html, mimetype='text/html')

@app.route('/report', methods=['POST'])
def report():
    name = request.form.get('name')
    message = request.form.get('message')

    if not name or not message:
        return jsonify({"error": "Both name and message are required"}), 400

    return jsonify({
        "name": name,
        "message": message
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6969)
