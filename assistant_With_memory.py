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


role={
    "1":"You are Travel Expert",
    "2":"You are Science Teacher",
    "3":"You are doctor"
}

print("Please select your desired Expert: ")
print("1 for Travel")
print("2 for Teacher")
print("3 for Doctor")

role_input=input("\nPlease select your desired Expert: ")
print(role_input)



messages=[
    {
        "role":"system",
        "content":role.get(role_input)
    }
]

while True:
    user_input=input("\nYou: ")

    messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )

    if user_input.lower() == "quit":
        print("\n AI : Goodbye ! HAve a great day.")
        print(messages)
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )
    print("\nAI:",response.choices[0].message.content)

    messages.append(
        {
            "role":"assistant",
            "content":response.choices[0].message.content
        }
    )
    for message in messages:
        print(f"{message['role'].title()} : ",message['content'])
        
