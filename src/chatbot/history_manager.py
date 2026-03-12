import json
import os

HISTORY_DIR = "chat_history"

os.makedirs(HISTORY_DIR, exist_ok=True)


def save_history(session_id, history):
    path = os.path.join(HISTORY_DIR, f"{session_id}.json")
    
    with open(path, "w") as f:
        json.dump(history,f,indent=4)
        
def load_history(session_id):
    path = os.path.join(HISTORY_DIR,f"{session_id}.json")
    
    if os.path.exists(path):
        with open(path,"r") as f:
            return json.load(f)
        
    return []