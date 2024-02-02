import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("PERPLEXITY_API_KEY")

url = "https://api.perplexity.ai/chat/completions"

payload = {
    "model": "mixtral-8x7b-instruct",
    "messages": [
        {
            "role": "system",
            "content": "Be precise and concise."
        },
        {
            "role": "user",
            "content": "How many stars are there in our galaxy?"
        }
    ]
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {API_KEY}"
}

response = requests.post(url, json=payload, headers=headers)

# print(response)

parsed_response = json.loads(response.text)
message_content = parsed_response['choices'][0]['message']['content']
print("Assistant Content:\n", message_content)

model = parsed_response['model']
usage = parsed_response['usage']
prompt_tokens = usage['prompt_tokens']
completion_tokens = usage['completion_tokens']
total_tokens = usage['total_tokens']

print("Model Used:\n", model)
print("Usage Statistics:\n")
print("\tPrompt Tokens:", prompt_tokens)
print("\tCompletion Tokens:", completion_tokens)
print("\tTotal Tokens:", total_tokens)