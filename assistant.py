from openai import OpenAI
from dotenv import load_dotenv
import os
import time


load_dotenv()

client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("="*40)
print("          My Ai Assistant")
print("="*40)

while True:
    user_input=input("\nYou: ")

    if user_input.lower() == "quit":
        print("\n AI : Goodbye ! HAve a great day.")
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role":"user",
                "content":user_input
            }
        ]
    )
    print("\nAI:",response.choices[0].message.content)
