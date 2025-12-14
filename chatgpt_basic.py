from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

# Simulate response
completion = {"choices":[{"message":{"content":"[Simulated AI response: What is AI?]"}}]}
print(completion["choices"][0]["message"]["content"])
