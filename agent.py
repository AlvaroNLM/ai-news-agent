from ner import extract_entities
from classifier import classify_text
from summarizer import summarize_text

class NewsAIAgent():
    def __init__(self, ner_name, classifier_name, summarizer_name):
        self.log = []
        self.ner_name = ner_name
        self.classifier_name = classifier_name
        self.summarizer_name = summarizer_name

    def think(self, message):
        print(f"[AGENT] {message}")
        self.log.append(message)

    def run(self, text):
        self.think("Extracting entities from text...")
        entities = extract_entities(text, self.ner_name)

        self.think("Classifying the text topic...")
        topic = classify_text(text, self.classifier_name)

        self.think("Summarizing the text...")
        summary = summarize_text(text, self.summarizer_name)

        return {
            "entities": entities,
            "topic": topic,
            "summary": summary
        }