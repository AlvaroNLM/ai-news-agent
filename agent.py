from ner import extract_entities
from classifier import classify_text
from summarizer import summarize_text

class NewsAIAgent:
    def __init__(self):
        self.log = []

    def think(self, message):
        print(f"[AGENT] {message}")
        self.log.append(message)

    def run(self, text):
        self.think("Extracting entities from text...")
        entities = extract_entities(text)

        self.think("Classifying the text topic...")
        topic = classify_text(text)

        self.think("Summarizing the text...")
        summary = summarize_text(text)

        return {
            "entities": entities,
            "topic": topic,
            "summary": summary
        }