import sqlite3
from langchain_core.documents import Document

def load_db(file_path):
    """
    Loads a SQLite .db file, reads all tables, and converts rows to Documents.
    """
    try:
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()
        
        # Get all table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        documents = []
        
        for table in tables:
            table_name = table[0]
            
            # Get columns
            # cursor.description is only available after a select
            cursor.execute(f"SELECT * FROM {table_name}")
            columns = [description[0] for description in cursor.description]
            
            # Fetch all rows (warning: might be large, but for mini project it's fine)
            rows = cursor.fetchall()
            
            for row in rows:
                row_content = []
                for i, col in enumerate(columns):
                    val = str(row[i]).strip()
                    if val:
                        row_content.append(f"{col}: {val}")
                
                content = "; ".join(row_content)
                if content:
                    meta = {
                        "source": file_path,
                        "table": table_name
                    }
                    documents.append(Document(page_content=content, metadata=meta))
                    
        conn.close()
        return documents

    except Exception as e:
        print(f"Error loading DB {file_path}: {e}")
        return []
