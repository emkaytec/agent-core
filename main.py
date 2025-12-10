import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

poem_prompt = """
Please write a poem about ChatGPT.
Ensure that the poem is written in basic English.
Ensure that the poem is written in a manner that a 4th grader would be able to
understand.
"""

story = "This is a string"

delimited_prompt = f"""Complete the story delimited by triple backticks.
```{story}```"""


def get_response(prompt: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content or ""


def main():
    response = get_response(poem_prompt)
    print(response)


if __name__ == "__main__":
    main()
