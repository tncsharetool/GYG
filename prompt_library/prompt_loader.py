# prompt_library/prompt_loader.py

import json

def load_travel_prompts(path="prompt_library/travel_prompts.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_viral_sources(path="prompt_library/viral_sources.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
