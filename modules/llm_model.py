import requests

# API Configuration
API_URL = "https://router.huggingface.co/together/v1/chat/completions"
API_TOKEN = "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"  # Replace with your actual token
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
}

def query(payload):
    """Query the Hugging Face API with the given payload."""
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def get_model_response(messages, model="mistralai/Mistral-7B-Instruct-v0.3"):
    """Get a response from the specified model."""
    response = query({
        "messages": messages,
        "model": model
    })
    return response["choices"][0]["message"]

