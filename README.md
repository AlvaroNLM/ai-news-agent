# News AI Agent

This project is an AI agent to analyze news.

- Entities extraction (NER)
- Topic classification (Zero-shot)
- Summary (Transformers)

## Execution

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python main.py
```

OR

fix ``run.py`` and 

```bash
python run.py
```

## Folder tree

news_ai_agent/
├── main.py
├── agent.py               # Lógica del agente (pipeline)
├── ner.py                 # Extracción de entidades
├── classifier.py          # Clasificador de temas
├── summarizer.py          # Resumen de texto
├── example_input.txt      # Uno o varios textos de prueba
├── README.md              # Breve explicación del proyecto
└── requirements.txt
