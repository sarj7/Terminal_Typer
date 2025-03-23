import requests
import json
import sys

class GeminiAPI:
    def __init__(self, api_key=None):
        self.api_key = api_key
        # Updated to use gemini-1.5-flash, which is likely available for free tier
        self.base_url = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent"
    
    def set_api_key(self, api_key):
        self.api_key = api_key
    
    def fetch_random_paragraph(self, prompt):
        if not self.api_key:
            raise ValueError("API key is not set.")
        
        typing_prompt = f"Generate a paragraph for typing practice about: {prompt}. Make it 3-4 sentences long."
        
        headers = {
            "Content-Type": "application/json"
        }
        
        data = {
            "contents": [
                {
                    "role": "user",  # Required field for Gemini API
                    "parts": [
                        {
                            "text": typing_prompt
                        }
                    ]
                }
            ],
            "generationConfig": {
                "temperature": 0.7,
                "topK": 40,
                "topP": 0.95,
                "maxOutputTokens": 200
            }
        }
        
        url = f"{self.base_url}?key={self.api_key}"
        
        try:
            print(f"Contacting Gemini API at: {self.base_url}")
            response = requests.post(url, headers=headers, json=data)
            
            if response.status_code != 200:
                print(f"API Error: Status code {response.status_code}")
                print(f"Response: {response.text}")
                return "The quick brown fox jumps over the lazy dog."
                
            response_data = response.json()
            print(f"Response structure preview: {list(response_data.keys())}")
            
            # Correct path for extracting text from Gemini API response
            if 'candidates' in response_data and len(response_data['candidates']) > 0:
                text = response_data['candidates'][0]['content']['parts'][0]['text']
                return text.strip()
            else:
                print("Unexpected response structure:", json.dumps(response_data, indent=2))
                return "The quick brown fox jumps over the lazy dog."  # Fallback text
            
        except Exception as e:
            print(f"Error fetching text: {e}")
            return "The quick brown fox jumps over the lazy dog."  # Fallback text