from transformers import pipeline

CANDIDATE_LABELS = ["politics", "economy", "technology", "sports", "health", "science"] # the topic as a label list

def classify_text(text, name_classifier):
    classifier = pipeline(name_classifier)
    result = classifier(text, CANDIDATE_LABELS)
    return result['labels'][0]  # max point label -> the topic