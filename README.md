# Book Recommender System

This project implements a book recommendation system using the BookCrossing dataset. The system provides personalized book recommendations based on user preferences, friends' reading habits, and similarities with other users.

## Features

### 1. Personalized Recommendations

- **Description**: Get recommendations based on your reading history.
- **Implementation**: Uses collaborative filtering and content-based filtering to suggest books similar to those you have liked or rated highly.

### 2. Friend-Based Recommendations

- **Description**: Discover trending books among your friends.
- **Implementation**: Compares your reading list with your friends' to suggest books that are popular within your social circle.

### 3. Interest-Based Recommendations

- **Description**: Explore books read by users with similar interests.
- **Implementation**: Uses Jaccard distance or other similarity measures to find users with overlapping reading preferences and recommends books they have enjoyed.

### 4. Interactive Interface

- **Description**: Provides an intuitive user interface using Streamlit.
- **Features**: Allows users to log in, add friends, and explore recommendations seamlessly.

### 5. Data Privacy

- **Description**: Respects user privacy and complies with GDPR.
- **Implementation**: Ensures that user data is pseudonymized and used only for generating recommendations.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/book-recommender-system.git
   cd book-recommender-system



# Rule Based Chatbot

This project implements a simple chatbot using Flask and a set of predefined rules stored in a JSON file. The chatbot responds to user input based on matching patterns defined in the rules.

## Features

### 1. Chat Interface

- **Description**: Provides a web-based chat interface where users can interact with the chatbot.
- **Usage**: Users can type messages into an input field and receive responses from the bot displayed on the web page.

### 2. Rule-based Responses

- **Description**: Generates responses based on predefined rules configured in a JSON file (`data.json`).
- **Implementation**: Matches user input against patterns defined in the rules and returns corresponding responses.

### 3. JSON Configuration

- **Description**: Configures chatbot rules using a JSON file for easy customization.
- **Format**: Each rule in `data.json` includes a `pattern` (string to match in user input) and a `response` (string response from the bot).

### 4. RESTful API

- **Description**: Includes an API endpoint `/get_response` to handle user input and return bot responses.
- **Usage**: Developers can integrate the chatbot into other applications by sending POST requests to `/get_response` with `user_input` in the request body.

### 5. Dynamic Interaction

- **Description**: Allows for real-time interaction between users and the chatbot through the web interface.
- **Features**: Supports continuous conversation where users can ask questions, receive answers, and engage in dialogue.

### 6. Easy Deployment

- **Description**: Deployable on local environments or cloud platforms.
- **Flexibility**: Runs with Python and Flask, making it easy to scale and adapt based on application requirements.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/flask-chatbot.git
   cd flask-chatbot

# Tic-Tac-Toe AI

This project implements a Tic-Tac-Toe game with an unbeatable AI agent using the Minimax algorithm with Alpha-Beta pruning. The game continues until the board is completely filled, after which the winner is announced.

## Features

- Play Tic-Tac-Toe against an AI opponent.
- The AI uses the Minimax algorithm with Alpha-Beta pruning to make optimal moves.
- The game board is displayed after each move.
- The game checks for a winner only after the board is completely filled.

## How to Play

1. The game starts with an empty Tic-Tac-Toe board.
2. Players take turns to place their marks (X for the human player and O for the AI) on the board.
3. The human player is prompted to enter their move.
4. The AI makes its move based on the Minimax algorithm.
5. The game continues until the board is completely filled.
6. After the board is full, the game announces the winner or declares a tie.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/tic-tac-toe-ai.git
   cd tic-tac-toe-ai
