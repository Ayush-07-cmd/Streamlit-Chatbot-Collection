import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey! 👋", "Greetings!", "Hey, nice to meet you!"],
    "how are you": ["I'm good, thanks!", "Doing great, and you?", "All good!", "Feeling fantastic today! 😊"],
    "what's your name": ["I'm your friendly chatbot!", "You can call me ChatBuddy 🤖", "I'm a simple bot made by Jaan!"],
    "bye": ["Goodbye!", "See you later!", "Bye! 👋", "Catch you soon!", "Take care!"],
    "thank you": ["You're welcome!", "No problem!", "Anytime!", "Happy to help! 🙌"],
    "thanks": ["You're welcome!", "Glad I could help!", "Don't mention it!"],
    "what can you do": ["I can chat with you!", "I'm here to make your day better! 😊", "Just a simple bot for fun!"],
    "i love you": ["Aww, that's sweet! ❤️", "Love you too!", "You're awesome!"],
    "who made you": ["I was created by Ayush!", "Ayush is my creator 💻", "I was coded by a cool developer(Ayush)...!!"],
    "good morning": ["Good morning! ☀️", "Wishing you a great day ahead!", "Morning!"],
    "good night": ["Good night! 🌙", "Sweet dreams!", "Sleep well!"],
    "tell me a joke": [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the computer go to the doctor? Because it had a virus!",
        "Why was the math book sad? It had too many problems. 😂"
    ],
    "default": ["I'm not sure I understand. Could you rephrase? 🤔", 
                "Hmm... that’s interesting. Tell me more!", 
                "Sorry, I didn’t get that. Try asking me something else!"]
}

def simple_chatbot(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])
