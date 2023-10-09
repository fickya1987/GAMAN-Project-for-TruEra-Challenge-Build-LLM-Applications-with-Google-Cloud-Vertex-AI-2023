import requests

# View our quick start guide to get your API key:
# https://developer.voiceflow.com/reference/overview
api_key = "{api_key}"

user_id = "user_123"  # Unique ID used to track conversation state
user_input = "Hello world!"  # User's message to your Voiceflow assistant

body = {"action": {"type": "text", "payload": "Hello world!"}}

# Start a conversation
response = requests.post(
    f"https://general-runtime.voiceflow.com/state/user/{user_id}/interact",
    json=body,
    headers={"Authorization": api_key},
)

# Log the response
print(response.json())
