from sentence_transformers import SentenceTransformer, util
import streamlit as st

@st.cache_resource
def load_bert_model():
    """Load and cache the BERT model for semantic similarity."""
    return SentenceTransformer('all-MiniLM-L6-v2')

def calculate_bert_similarity(resume_text, job_description):
    """
    Calculate semantic similarity score using BERT embeddings.
    Returns a score between 0 and 100.
    """
    if not job_description or not resume_text:
        return 0.0
        
    model = load_bert_model()
    
    # Compute embeddings
    # We truncate to avoid exceeding model limits if text is huge, 
    # though MiniLM handles reasonably large context, it's safer to not crash.
    # But usually resumes fit.
    
    embedding_resume = model.encode(resume_text, convert_to_tensor=True)
    embedding_jd = model.encode(job_description, convert_to_tensor=True)
    
    # Calculate cosine similarity
    similarity = util.cos_sim(embedding_resume, embedding_jd)
    
    # Convert to percentage
    score = similarity.item() * 100
    return max(0, min(100, score))
