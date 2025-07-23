from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# Dynamic route
@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

# POST endpoint
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name', 'Anonymous')
    return jsonify({
        "message": f"Data received for {name}",
        "status": "success"
    })

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)