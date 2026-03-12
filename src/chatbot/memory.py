import json
import os

class ConversationMemory:
    def __init__(self):
        self.history = []
        
    def add_turn(self, user_input, bot_response):
        self.history.append({
                "user":user_input,
                "bot": bot_response
            })
    
    def get_history(self):
        return self.history    
        
    def get_formatted_history(self):
        formatted = ""
        for turn in self.history:
            formatted += f"User : {turn['user']}\n Assistant : {turn['bot']}\n"
        
        return formatted
    
    def get_conversation_text(self):
        text=""
        for turn in self.history:
            text += f"User : {turn['user']}\nAssistant : {turn['bot']}\n\n"
        
        return text

    def save_to_json(self, filepath):
        """Save history to a JSON file."""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w') as f:
            json.dump(self.history, f, indent=4)
            
    def load_from_json(self, filepath):
        """Load history from a JSON file."""
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                try:
                    self.history = json.load(f)
                except json.JSONDecodeError:
                    self.history = []
        else:
            self.history = []