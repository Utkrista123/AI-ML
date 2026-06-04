from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key= os.getenv("GROQ_API_KEY")
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful chatbot."
    }
]

while True:
    user_input = input("You: ")

    messages.append(
        {
            "role":"system",
            "content": user_input
        }
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        messages= messages
    )

    ai_reply = response.choices[0].message.content
    
    print("AI: ", ai_reply)

    messages.append(
        {
            "role":"assistant",
            "content": ai_reply
        }
    )

