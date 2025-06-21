from transformers import pipeline
summarizer = pipeline("summarization")

def summarize_text(text):
    if len(text) > 1000:
        text = text[:1000]  # to limit the size
    return summarizer(text, max_length=120, min_length=30, do_sample=False)[0]['summary_text']
