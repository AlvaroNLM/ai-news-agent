import os
from datetime import datetime
from agent import NewsAIAgent
from newspaper import Article
import json

# get news from url
def get_text_from_url(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

# generate otuput
def save_output_to_file(output_str: str, folder="data_dst"):
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}.txt"
    filepath = os.path.join(folder, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(output_str)
    return filepath

def read_json(json_file=os.path.join(os.path.join(os.getcwd(), "data_src"), "data.json")):
    with open(json_file, "r") as f:
        my_dict = json.load(f)
        file = my_dict["file"]
        ner_name = my_dict["ner_name"]
        classifier_name = my_dict["classifier_name"]
        summarizer_name = my_dict["summarizer_name"]
    return file, ner_name, classifier_name, summarizer_name

if __name__ == "__main__":
    # From text
    # file_name, ner_name, classifier_name, summarizer_name = read_json()
    # with open(file_name, "r", encoding="utf-8") as f:
    #     input_text = f.read()
    
    # From url
    _, ner_name, classifier_name, summarizer_name = read_json()
    url = input("Please, paste here the url link that is ready to be analyzed: ").strip()
    input_text = get_text_from_url(url)

    agent = NewsAIAgent(ner_name, classifier_name, summarizer_name)
    result = agent.run(input_text)

    output_str = (
        "===== Results =====\n\n"
        ">> Entities:\n"
        + "\n".join([f"{ent[0]} ({ent[1]})" for ent in result['entities']])
        + "\n\n>> Classified topic:\n"
        + result['topic']
        + "\n\n>> Summary:\n"
        + result['summary']
    )

    # print
    print("\n===== Results =====")
    print("\n>> Entities:")
    print(result['entities'])

    print("\n>> Classified topic:")
    print(result['topic'])

    print("\n>> Summary:")
    print(result['summary'])

    # -> to file.txt
    saved_path = save_output_to_file(output_str)
    print(f"Result at: {saved_path}")