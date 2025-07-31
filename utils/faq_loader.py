import json
import os

def load_faq_data():
    faq_path = os.path.join("data", "faq_data.json")
    with open(faq_path, "r", encoding="utf-8") as f:
        return json.load(f)
