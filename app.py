import streamlit as st
from bot import get_response  # Importing the function from bot.py
from datetime import datetime

# Title and description for the Streamlit app
st.title("Advanced Chatbot")
st.header("Welcome to the Enhanced Chatbot")
st.text("Type something and I'll respond with timestamps.")

# Initialize chat history in session state if not already present
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Display previous chat messages with timestamps
for message in st.session_state['chat_history']:
    st.write(message)

# User input
user_input = st.text_input("You: ", "")

# Handle user input and generate response
if user_input:
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append the user input to the chat history with timestamp
    st.session_state['chat_history'].append(f"[{timestamp}] You: {user_input}")
    
    # Get the chatbot's response from bot.py
    response = get_response(user_input)
    
    # Append the bot's response to the chat history with timestamp
    st.session_state['chat_history'].append(f"[{timestamp}] Bot: {response}")
    
    # Display updated chat history with the new message
    for message in st.session_state['chat_history']:
        st.write(message)
