import streamlit as st
import ollama

# Sample conversation context (customize as needed)
messages = [
    {"role": "system", "content": "You are a helpful mental health support assistant."},
    {"role": "user", "content": "I feel anxious and can't focus. What should I do?"}
]




st.set_page_config(page_title="🧠 Mental Health Chatbot")

st.title("🧠 Mental Health Support Chatbot")

# Define safe system prompt
SYSTEM_PROMPT = """
You are a supportive, empathetic mental health assistant.
You are not a therapist or doctor.
Always encourage kindness, self-care, and professional help when needed.
"""

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

# Show chat history
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

# Input box
user_input = st.chat_input("Type your feelings or thoughts here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ollama.chat(
                model="llama3",  # or "mistral", "phi3" etc.
                messages=st.session_state.messages
            )
            reply = response["message"]["content"]
            st.write(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
