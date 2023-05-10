#created an AI that helps answer Mental Health

import openai
import os

#setting key
os.environ["OPENAI_API_KEY"] = "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"

# Set up OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Prompt the user to input their feeling
user_question = input("How are you feeling? ")

# Define a prompt for the OpenAI API to generate a response based on the user's question
prompt = (f"Generate a response about {user_question} in the context of mental health.")

# Generate a response from OpenAI's GPT-3 model
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the generated response
print(response.choices[0].text)
