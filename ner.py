import spacy

def extract_entities(text, ner_name="en_core_web_sm"):
    nlp = spacy.load(ner_name) # previously-installed by: python -m spacy download en_core_web_sm
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]