from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

messages = [{"role":"system","content":"You are a helpful assistant."}]

print("ChatGPT Console Chat (type 'quit' to exit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    messages.append({"role":"user","content":user_input})
    assistant_message = f"[Simulated Secure Response for: '{user_input}']"
    messages.append({"role":"assistant","content":assistant_message})
    print(f"AI: {assistant_message}\n")
