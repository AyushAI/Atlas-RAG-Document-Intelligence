from langchain_core.prompts import PromptTemplate
from src.summarizer.summary_styles import SUMMARY_STYLES
from src.summarizer.summary_propmpt import BASE_SUMMARY_PROMPTS
from src.rag.gemini_llm import generate_response

def summarize_document(text, style="bullet", custom_instructions=None):
    
    if custom_instructions:
        instruction = custom_instructions
    else:
        instruction = SUMMARY_STYLES.get(style, SUMMARY_STYLES["bullet"])
        
    prompt = PromptTemplate.from_template(BASE_SUMMARY_PROMPTS)
    
    final_prompt = prompt.format(
        context = text,
        instruction=instruction
    )
    
    res, usage = generate_response(final_prompt)
    
    return res, usage