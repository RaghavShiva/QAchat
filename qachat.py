from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    # This function remains the same as it correctly sends the message and streams the response
    response = chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit and input:
    response_chunks = get_gemini_response(input) # Get the streamed response
    
    # Add user query to session state chat history immediately
    st.session_state['chat_history'].append(("You", input))
    
    st.subheader("The Response :")
    
    full_response_text = "" # Initialize an empty string to accumulate the full response
    for chunk in response_chunks:
        full_response_text += chunk.text # Append each chunk to the full response string
    
    st.write(full_response_text) # Write the complete response
    st.session_state['chat_history'].append(("Bot", full_response_text)) # Add the complete response to history

st.subheader("Your Chat History :")
    
for role, text in st.session_state['chat_history']:
    st.write(f"**{role}**: {text}") # Bold the role for better readability
