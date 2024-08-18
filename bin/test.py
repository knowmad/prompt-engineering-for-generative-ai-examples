import os
import openai

# Retrieve the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

# Extract the content of the response
haiku = completion.choices[0].message.content

# Format the haiku by stripping leading/trailing whitespace and printing each line
formatted_haiku = "\n".join(line.strip() for line in haiku.splitlines())

print(formatted_haiku)
