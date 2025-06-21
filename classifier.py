from transformers import pipeline
classifier = pipeline("zero-shot-classification")

CANDIDATE_LABELS = ["politics", "economy", "technology", "sports", "health", "science"] # the topic as a label list

def classify_text(text):
    result = classifier(text, CANDIDATE_LABELS)
    return result['labels'][0]  # max point label -> the topic