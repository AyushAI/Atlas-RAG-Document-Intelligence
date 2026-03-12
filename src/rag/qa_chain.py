from langchain_core.prompts import PromptTemplate
from src.rag.prompt_templates import RAG_PROMPT
from src.rag.retriever import get_retriever
from src.rag.gemini_llm import generate_response

def ask_question(question:str, db_path:str="vector_db", model: str = "models/gemini-3-flash-preview"):
    retriever = get_retriever(db_path)
    
    docs = retriever.invoke(question) 
    context = "\n\n".join([d.page_content for d in docs])
    
    prompt = PromptTemplate.from_template(RAG_PROMPT)

    final_prompt = prompt.format(context=context, question = question)
    
    answer, usage = generate_response(final_prompt, model=model)
    
    return answer, docs, usage