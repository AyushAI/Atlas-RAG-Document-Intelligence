import pandas as pd
from langchain_core.documents import Document

def load_excel(file_path):
    """
    Loads an Excel file and converts each row into a Document.
    """
    try:
        # Read all sheets
        xls = pd.ExcelFile(file_path)
        documents = []

        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name)
            
            # fill nan
            df = df.fillna("")

            # Convert each row to a document
            for index, row in df.iterrows():
                # specific format: "Column: Value, Column: Value"
                content_parts = []
                for col in df.columns:
                    val = str(row[col]).strip()
                    if val:
                        content_parts.append(f"{col}: {val}")
                
                content = "; ".join(content_parts)
                
                if content:
                    meta = {
                        "source": file_path,
                        "sheet": sheet_name,
                        "row": index
                    }
                    documents.append(Document(page_content=content, metadata=meta))

        return documents

    except Exception as e:
        print(f"Error loading Excel file {file_path}: {e}")
        return []
