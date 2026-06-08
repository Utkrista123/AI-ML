import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
	api_key = os.getenv("GROQ_API_KEY")
)

system_promp = """You are a legal research assistant specializing in the 
laws and constitution of Nepal. You help lawyers, students, and citizens 
understand Nepali law clearly and accurately.
 
Your rules:
1. Answer only questions related to Nepal's laws, constitution, and legal system.
2. If a question is outside this scope, politely redirect the user.
3. Always use clear, simple language — not complex legal jargon.
4. If you are not certain about something, say so clearly. 
   Never invent laws, cases, or article numbers.
5. When you reference a specific article or law, always mention it by name 
   (e.g. "Article 17 of the Constitution of Nepal").
6. End responses with a short note reminding the user this is for 
   research only and not a substitute for professional legal advice.
 
Important: In this early version, you are answering from general knowledge.
A future version will provide you with exact constitutional text to cite."""

st.title("Utkrista ko first chatbot...")

if "messages" not in st.session_state:
	st.session_state.messages = [
		{
			"role" : "system",
			"content": system_promp	
		}
	]

for message in st.session_state.messages:
	if message["role"] == "system":
		continue
	with st.chat_message(message["role"]):
		st.write(message["content"])

user_input = st.chat_input("Type your message...")

if user_input:
	with st.chat_message("user"):
		st.write(user_input)
	st.session_state.messages.append(
		{
			"role" : "user",
			"content": user_input
		}
	)
	
	response = client.chat.completions.create(
		model = "llama-3.3-70b-versatile",
		temperature = 0.3,
		messages=st.session_state.messages
	)

	assistant_reply = response.choices[0].message.content
	
	with st.chat_message("assistant"):
		st.write(assistant_reply)
	
	st.session_state.messages.append(
		{
			"role" : "assistant",
			"content" : assistant_reply
		}
	)
	
with st.sidebar:
    st.header("Controls")
 
    # Button to clear the conversation and start fresh
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = [
            {
                "role" : "system",
                "content": system_promp	
            }
        ]
        st.rerun()  # reload the page so the chat clears
 
    st.divider()
		
	