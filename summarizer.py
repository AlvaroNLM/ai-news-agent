from transformers import pipeline

def summarize_text(text, name_summarizer):
    summarizer = pipeline(name_summarizer)
    if len(text) > 1000:
        text = text[:1000]  # to limit the size
    return summarizer(text, max_length=120, min_length=30, do_sample=False)[0]['summary_text']
