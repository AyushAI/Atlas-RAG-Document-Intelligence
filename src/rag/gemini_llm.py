from google import genai
import os

# Using the key provided by the user (FML...f3E)
client = genai.Client(api_key="Your API Key")

def generate_response(prompt:str, model: str = "models/gemini-3-flash-preview"):
    try:
        response = client.models.generate_content(
            model=model, 
            contents=prompt
        )
        
        # We still return usage metadata (empty or extracted) to keep the app from crashing
        usage = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
        if hasattr(response, "usage_metadata") and response.usage_metadata:
            usage["prompt_tokens"] = response.usage_metadata.prompt_token_count
            usage["completion_tokens"] = response.usage_metadata.candidates_token_count
            usage["total_tokens"] = response.usage_metadata.total_token_count
            
        return response.text, usage
    
    except Exception as e:
        print(f"Gemini API Error with model {model} : {e}")
        return f"⚠️ API Error: {e}. Please ensure your key has quota for {model}.", {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}