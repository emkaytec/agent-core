import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant that can answer questions and help with tasks."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
