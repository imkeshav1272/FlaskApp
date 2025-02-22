from flask import Flask, jsonify
import json

app = Flask(__name__)

# Define the /api route
@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/api', methods=['GET'])
def get_data():
    try:
        # Open the data file and load JSON data
        with open('data.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        # In case of an error (e.g., file not found or read error)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

  
  