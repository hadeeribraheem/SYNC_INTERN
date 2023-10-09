# ChatBot

ChatBot is a simple Python program that uses a JSON file to store intents and responses. It utilizes the difflib library to find the best match for user input and provides appropriate responses based on the matched intent.

## Features

- Loads intents and responses from a JSON file.
- Uses fuzzy matching to find the best match for user input.
- Allows users to teach the bot new responses for unmatched input.
- Saves the updated intents to the JSON file for future use.

## Requirements

- Python 3.x
- `json` module
- `difflib` module

## Usage

1. Clone the repository or download the code files.
2. Make sure you have the required dependencies installed.
3. Run the `ChatBot.py` script.
4. Enter your input when prompted by the chatbot.
5. To quit the chatbot, type "quit".

## Configuration

The chatbot relies on a JSON file (`intents.json`) to store the intents and responses. You can modify this file to add new patterns and responses as needed. Each intent in the JSON file consists of an array of patterns and an array of responses.

```json
{
    "intents": [
        {
            "patterns": ["Hello", "Hi", "Hey"],
            "responses": ["Hi there!", "Hello!", "Hey! How can I help you?"]
        },
        {
            "patterns": ["What is your name?", "Who are you?"],
            "responses": ["I am a chatbot!", "My name is ChatBot."]
        },
        ...
    ]
}
```

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.


