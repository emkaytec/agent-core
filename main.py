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

one_shot_prompt = """
    Q: Sum the numbers 3, 5, and 6.  A: The sum of 3, 5, and 6 is 14.
    Q: Sum the numbers 2, 4, and 7.  A:
"""

few_shot_prompt = """
    Text: Today the weather is fantastic -> Classification: positive
    Text: The furniture is small -> Classification: neutral
    Text: I don't like your attitude -> Classification: negative
    Text: That shot selection was awful -> Classification: 
"""


def get_response(prompt: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-5.1", messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content or ""


def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # response = get_response(few_shot_prompt)
    response = client.chat.completions.create(
        model="gpt-5.1",
        messages = [
            {"role": "user", "content": "Today the weather is fantastic"},
            {"role": "assistant", "content": "positive"},
            {"role": "user", "content": "The furniture is small"},
            {"role": "assistant", "content": "neutral"},
            {"role": "user", "content": "I don't like your attitude"},
            {"role": "assistant", "content": "negative"},
            {"role": "user", "content": "That shot selection was awful"}
        ],
        temperature=0
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
