import csv
import os
import datetime

LOG_DIR = "logging"
LOG_FILE = "chat_logs.csv"

class Logger:
    def __init__(self, log_dir=LOG_DIR, log_file=LOG_FILE):
        self.log_path = os.path.join(log_dir, log_file)
        os.makedirs(log_dir, exist_ok=True)
        self._init_log_file()

    def _init_log_file(self):
        """Initialize the log file with headers if it doesn't exist."""
        if not os.path.exists(self.log_path):
            with open(self.log_path, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    "timestamp", 
                    "username", 
                    "query", 
                    "response", 
                    "latency_ms", 
                    "prompt_tokens", 
                    "completion_tokens", 
                    "total_tokens", 
                    "model"
                ])

    def log_interaction(self, username, query, response, latency_ms, 
                        prompt_tokens=0, completion_tokens=0, total_tokens=0, model="gemini-2.0-flash"):
        """Log a chat interaction."""
        timestamp = datetime.datetime.now().isoformat()
        
        try:
            with open(self.log_path, mode='a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    timestamp,
                    username,
                    query,
                    response,
                    f"{latency_ms:.2f}",
                    prompt_tokens,
                    completion_tokens,
                    total_tokens,
                    model
                ])
        except Exception as e:
            print(f"Error logging interaction: {e}")

# Global logger instance
logger = Logger()
