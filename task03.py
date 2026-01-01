import spacy
from transformers import pipeline

# 1. Load SpaCy for Entity Extraction
nlp = spacy.load("en_core_web_sm")

# 2. Load Transformer Pipeline for Summarization 
# We use 'sshleifer/distilbart-cnn-12-6' because it's fast and accurate
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def analyze_legal_document(text):
    print("\n--- Processing Document ---")
    
    # --- PART 1: Information Extraction (SpaCy) ---
    doc = nlp(text)
    entities = {"Parties": [], "Dates": [], "Laws": []}
    
    for ent in doc.ents:
        if ent.label_ in ["ORG", "PERSON"]:
            entities["Parties"].append(ent.text)
        elif ent.label_ == "DATE":
            entities["Dates"].append(ent.text)
        elif ent.label_ == "LAW":
            entities["Laws"].append(ent.text)

    # --- PART 2: Summarization (Transformers) ---
    # Legal docs are long; we limit the summary length
    summary = summarizer(text, max_length=50, min_length=20, do_sample=False)
    
    # --- Output Results ---
    print(f"Key Parties: {set(entities['Parties'])}")
    print(f"Key Dates: {set(entities['Dates'])}")
    print(f"\nAI Summary: {summary[0]['summary_text']}")

# Example: A complex legal-sounding clause
legal_contract = """
This Agreement is entered into on this 1st day of January, 2024, by and between 
Global Tech Corp and Sterling Law Firm. Under the terms of Section 4.2, the 
receiving party shall maintain the confidentiality of all proprietary information 
and shall not disclose such information to any third party for a period of 
five years following the termination of this agreement. Failure to comply 
will result in immediate legal action under the jurisdiction of New York State Law.
"""

analyze_legal_document(legal_contract)