import streamlit as st
import time
from langchain_ollama import OllamaLLM

# Initialize the Ollama LLM
model = OllamaLLM(model="qwen2.5-coder:latest")

st.title("Chat with Ollama LLM")

# Initialize chat history if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from the history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def generate_response(prompt):
    try:
        # Generate response using OllamaLLM
        response = model.invoke(prompt)
        return response
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
        return "Sorry, there was an error generating the response."

# Handle user input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display assistant response    
    with st.chat_message("assistant"):
        response = generate_response(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
