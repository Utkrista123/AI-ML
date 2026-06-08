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

    if user_input.lower() == "clear":
        del messages[1:]

    if user_input.lower() == "history":
        print(messages)

    if user_input.lower() == "help":
        print("Type 'clear' to clears conversation history. \n Type 'history' to prints all messages.")

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

