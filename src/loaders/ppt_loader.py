from langchain_core.documents import Document
import os

def load_ppt(file_path):
    """
    Loads a legacy .ppt file.
    Note: Full support for .ppt requires heavy dependencies like LibreOffice or COM automation (Windows).
    For now, this is a placeholder/stub or we can try basic binary string extraction if needed.
    """
    try:
        # Placeholder for complex .ppt handling
        # For now, we return a document stating it's not fully supported or try a basic text extraction?
        # Let's try to extract ascii strings as a fallback
        
        with open(file_path, "rb") as f:
            content = f.read()
            # Extract printable strings (naive approach)
            text = "".join([chr(b) for b in content if 32 <= b <= 126 or b in (10, 13)])
            
        return [Document(page_content=text, metadata={"source": file_path, "note": "Extracted via basic string analysis (legacy format)"})]

    except Exception as e:
        print(f"Error loading PPT {file_path}: {e}")
        return []
