import streamlit as st 
import os
from dotenv import load_dotenv
from chatbot import Chatbot
from helper import clean_input

load_dotenv()
st.set_page_config(page_title="Gemini CHATBOT")

bot = Chatbot(os.getenv("GEMINI_API_KEY"))

if "history" not in st.session_state:
    st.session_state.history = []

st.title("Welcome to Chatbot")

user_input = st.text_input("You")

if st.button("text"):
    try:
        message = clean_input(user_input)
        reply = bot.reply(message)
        st.session_state.history.append(("You", message))
        st.session_state.history.append(("Bot", reply))
    except Exception as e:
        if "429" in str(e):
            st.error("Slow down! You've hit the free tier limit. Please wait a minute before sending another message.")
        else:
            st.error(f"An error occurred: {e}")
    
for role, msg in st.session_state.history:
    st.write(f"**{role}:** {msg}")
        


