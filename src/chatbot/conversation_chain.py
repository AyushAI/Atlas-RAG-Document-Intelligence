from src.rag.qa_chain import ask_question
from src.rag.gemini_llm import generate_response

from src.rag.prompt_templates import CHAT_PROMPT

def chat_with_memory(question, memory, db_path="vector_db", model: str = "models/gemini-3-flash-preview"):
    
    rag_answer, docs, rag_usage = ask_question(question, db_path, model=model)
    
    history_text = memory.get_formatted_history()
    
    final_prompt = CHAT_PROMPT.format(
        history = history_text,
        question = question,
        rag_answer = rag_answer
    )
    
    final_anwer, chat_usage = generate_response(final_prompt, model=model)
    
    # Aggregate usage
    total_usage = {
        "prompt_tokens": rag_usage.get("prompt_tokens", 0) + chat_usage.get("prompt_tokens", 0),
        "completion_tokens": rag_usage.get("completion_tokens", 0) + chat_usage.get("completion_tokens", 0),
        "total_tokens": rag_usage.get("total_tokens", 0) + chat_usage.get("total_tokens", 0)
    }
    
    memory.add_turn(question, final_anwer)
    
    return final_anwer, docs, total_usage