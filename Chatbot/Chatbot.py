import json
from difflib import get_close_matches

class ChatBot:
    def __init__(self, intents_file):
        self.intents_file = intents_file
        self.intents = self.load_intents()

    def load_intents(self):
        with open(self.intents_file, 'r') as file:
            data = json.load(file)
        return data

    def save_intents(self):
        with open(self.intents_file, 'w') as file:
            json.dump(self.intents, file, indent=2)

    def find_best_match(self, user_question, questions):
        matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
        return matches[0] if matches else None

    def get_answer(self, question):
        for intent in self.intents["intents"]:
            if question in intent["patterns"]:
                return intent["responses"][0]

    def chat(self):
        while True:
            user_input = input("You: ")

            if user_input.lower() == "quit":
                break

            best_match = self.find_best_match(user_input, [q for intent in self.intents["intents"] for q in intent["patterns"]])
            if best_match:
                answer = self.get_answer(best_match)
                print(f"Bot: {answer}")
            else:
                print("Bot: I don't know the answer. Can you teach me?")
                new_answer = input('Type the answer or "skip" to skip: ')

                if new_answer.lower() != "skip":
                    new_block = {
                        "patterns": [user_input],
                        "responses": [new_answer]
                    }
                    self.intents["intents"].append(new_block)
                    self.save_intents()
                    print('Bot: Thank you! I learned a new response!')

if __name__ == "__main__":
    chatbot = ChatBot('intents.json')
    chatbot.chat()