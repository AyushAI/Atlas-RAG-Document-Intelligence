from langchain_core.documents import Document
from google import genai
from google.genai import types
import PIL.Image
import os
import io

def load_image(file_path):
    """
    Loads an image file and uses Gemini Vision to extract text and describe charts/graphs.
    """
    try:
        # Check for API key
        if not os.environ.get("GOOGLE_API_KEY"):
             # Fallback or error if no key. 
             # Assuming key is in env as per our plan (we need to migrate the hardcoded one later)
             # For now, I'll use the client if I can import it, or just re-instantiate with the hardcoded key 
             # from the existing codebase to ensure it works immediately, then we refactor.
             # Actually, better to import the client from src.rag.gemini_llm to reuse the key/config.
             pass

        from src.rag.gemini_llm import client 

        # Open image
        img = PIL.Image.open(file_path)
        
        prompt = """
        Analyze this image in detail.
        1. Extract all visible text.
        2. If there are charts, graphs, or tables, describe their data trends, axes, and key insights in detail.
        3. Describe any visual elements.
        """

        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=[prompt, img]
        )
        
        text_content = response.text
        
        return [Document(page_content=text_content, metadata={"source": file_path})]

    except Exception as e:
        print(f"Error loading Image {file_path}: {e}")
        return []
