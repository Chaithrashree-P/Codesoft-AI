import json

# Function to find response based on input
def get_response(input_text, rules):
    for rule in rules:
        if rule['pattern'] in input_text.lower():
            return rule['response']
    return "I'm sorry, I don't understand that."

# Load rules from JSON file
def load_rules(filename):
    with open(filename, 'r') as file:
        rules = json.load(file)
    return rules['rules']

# Initialize rules
rules = load_rules('data.json')

# Main function (optional)
if __name__ == '__main__':
    while True:
        user_input = input("You: ")
        response = get_response(user_input, rules)
        print("Bot:", response)
