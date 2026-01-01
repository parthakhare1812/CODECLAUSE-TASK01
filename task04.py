import cv2
import pytesseract
import spacy
from pyresparser import ResumeParser
import os

# 1. Computer Vision: Convert CV Image/PDF to Text
def extract_text_from_cv(image_path):
    # Load image using OpenCV
    img = cv2.imread(image_path)
    # Convert to grayscale for better OCR accuracy
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Perform OCR
    text = pytesseract.image_to_string(gray)
    return text

# 2. NLP: Analyze Text for Personality Traits
def predict_personality(cv_data):
    # Dictionaries of keywords associated with Big Five traits
    traits_keywords = {
        "Openness": ["creative", "innovative", "curious", "flexible", "research", "travel"],
        "Conscientiousness": ["organized", "disciplined", "detail-oriented", "punctual", "management"],
        "Extraversion": ["leadership", "teamwork", "public speaking", "social", "outgoing", "sales"],
        "Agreeableness": ["collaborative", "kind", "supportive", "empathy", "volunteer", "team"],
        "Neuroticism": ["stress", "anxious", "reactive", "pressure", "uncertainty"] # Usually negative mapping
    }

    scores = {trait: 0 for trait in traits_keywords}
    text = cv_data.lower()

    # Calculate scores based on keyword frequency
    for trait, keywords in traits_keywords.items():
        for word in keywords:
            if word in text:
                scores[trait] += 1
    
    return scores

# 3. Main Execution
if __name__ == "__main__":
    # Example Path (Ensure you have a sample_cv.png in your folder)
    cv_file = "sample_cv.png"
    
    if os.path.exists(cv_file):
        print("Extracting data from CV...")
        extracted_text = extract_text_from_cv(cv_file)
        
        print("Analyzing personality traits...")
        personality_results = predict_personality(extracted_text)
        
        print("\n--- Personality Profile (OCEAN Score) ---")
        for trait, score in personality_results.items():
            print(f"{trait}: {score}")
    else:
        print("File not found. Please provide a valid CV image.")