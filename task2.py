import re

def get_response(user_input):
    # Define a set of patterns and responses
    responses = {
        r'\bhello\b': "Hi there! How can I help you today?",
        r'\bhi\b': "Hello! What can I do for you?",
        r'\bhow are you\b': "I'm just a bot, but I'm doing great! How about you?",
        r'\bwhat is your name\b': "I am a simple chatbot created by you!",
        r'\bbye\b': "Goodbye! Have a great day!",
        r'\b(.*) (your|my) name\b': "I'm just a bot without a name.",
        r'\b(.*) (thank|thanks)\b': "You're welcome! If you have more questions, just ask.",
    }
    
    # Iterate over the patterns and match with user input
    for pattern, response in responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

    return "I'm sorry, I don't understand that."

def chatbot():
    print("Hello! I am your friendly chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if re.search(r'\bbye\b', user_input, re.IGNORECASE):
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
