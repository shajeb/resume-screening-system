import json

def save_json(path, text):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(text, f)