from flask import Flask, render_template, request, jsonify
import json
from bot import get_response

app = Flask(__name__)

# Load rules from JSON file
def load_rules(filename):
    with open(filename, 'r') as file:
        rules = json.load(file)
    return rules['rules']

rules = load_rules('data.json')

# Home route - serves the chat interface
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint to handle user input and return bot response
@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_input = request.json['user_input']
    response = get_response(user_input, rules)
    return jsonify({'bot_response': response})

if __name__ == '__main__':
    app.run(debug=True)
