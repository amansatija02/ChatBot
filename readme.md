# Gemini Chatbot (Python + Streamlit)

## Project Goal
Build a complete Python application that integrates a user interface, application logic, and an external AI API to understand how real Python applications are structured.

## What This Project Does
- Provides a chat-based UI using Streamlit
- Accepts user input and validates it
- Sends prompts to the Gemini API
- Displays AI-generated responses
- Maintains conversation history during a session

## Technologies Used
- Python
- Streamlit
- Google Gemini API
- Environment variables (.env)
- Tools: git,github

## Project Structure
- app.py: Streamlit application entry point
- chatbot.py: Core chatbot logic and API interaction
- helper.py: Input validation and helper functions

## What I Learned
- Structuring Python projects into logical modules
- Integrating third-party APIs in Python
- Managing application state using Streamlit session state
- Using environment variables securely
- Writing clean, reusable functions and classes
- Handling runtime errors gracefully

## Limitations 
- Chat history is session-based and not persisted
- No authentication or rate limiting
- Single-user focus

## Key Takeaway
This project taught me how to build a complete, interactive Python application and reinforced best practices for structure, state management, and external API integration.
