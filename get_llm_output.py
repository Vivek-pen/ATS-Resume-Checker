import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def get_llm_output(prompt, pdf_text=None):
    """
    Get response from OpenRouter using OpenAI client.
    
    Args:
        prompt (str): The instruction/prompt for the model.
        pdf_text (str): The text content from the PDF or other context.
        
    Returns:
        str: The model's response text.
        
    Note: Function signature changed to (prompt, pdf_text) to match typical LLM usage pattern 
    where prompt is primary.
    """
    # Initialize OpenAI client pointing to OpenRouter
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("API_KEY"),
    )
    
    content = []
    if prompt:
        content.append({"type": "text", "text": prompt})
    
    # Append pdf_text if provided
    if pdf_text:
        content.append({"type": "text", "text": f"\n\nContext/Resume Content:\n{pdf_text}"})

    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "https://localhost:8501", # Optional, for OpenRouter rankings
            "X-Title": "ATS Resume Checker", # Optional
        },
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": content
            }
        ]
    )
    
    return completion.choices[0].message.content
