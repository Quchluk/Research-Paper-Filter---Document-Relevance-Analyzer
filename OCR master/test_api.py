import os
from dotenv import load_dotenv
import requests

# Load environment variables (force reload)
load_dotenv(override=True)

api_key = os.getenv('OPENROUTER_API_KEY')
print(f"API Key loaded: {api_key[:20]}...")

# Test DeepSeek V3.2 model
try:
    print("\nTesting DeepSeek V3.2 model on OpenRouter...")
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek/deepseek-v3.2-exp",
            "messages": [
                {"role": "user", "content": "Say only the number 1"}
            ],
            "max_tokens": 10
        },
        timeout=30
    )
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        print(f"Success! Response: {result['choices'][0]['message']['content']}")
    else:
        print(f"Error Response: {response.text}")
        
except Exception as e:
    print(f"Exception: {e}")
