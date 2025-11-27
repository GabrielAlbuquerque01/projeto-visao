import json
import base64
import re
import string

def get_image_id(image_name : str):

    image_id = image_name.split('_')[-1].split('.')[0]

    cleaned_image_id = ''
    for i,c in enumerate(image_id):

        if c != '0':
            cleaned_image_id = image_id[i:]
            break

    return cleaned_image_id


def encode_image(image_path: str):

    with open(image_path, "rb") as f:
        image_bytes = f.read()

    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    return image_base64


def load_json(path_json : str):

    with open(path_json, 'r', encoding='utf-8') as f:
        json_loaded = json.load(f)

    return json_loaded


NUMBER_MAP = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
    "ten": "10"
}

CONTRACTIONS = {
    "dont": "don't", "doesnt": "doesn't", "cant": "can't",
    "couldnt": "couldn't", "shouldnt": "shouldn't",
    "wouldnt": "wouldn't", "isnt": "isn't", "arent": "aren't",
    "wasnt": "wasn't", "werent": "weren't",
    "im": "i'm", "ive": "i've", "ill": "i'll",
    "youre": "you're", "youve": "you've", "youll": "you'll",
    "theyre": "they're", "weve": "we've", "were": "we're"
}

ARTICLES = {"a", "an", "the"}

def normalize_answer_vqa(ans: str) -> str:
    if not isinstance(ans, str):
        return ans

    ans = ans.lower().strip()
    ans = re.sub(r'(?<!\d)\.(?!\d)', '', ans)
    ans = " ".join(NUMBER_MAP.get(w, w) for w in ans.split())
    ans = " ".join(w for w in ans.split() if w not in ARTICLES)

    for wrong, right in CONTRACTIONS.items():
        ans = ans.replace(wrong, right)

    ans = re.sub(r'(?<!\d),(?!\d)', ' ', ans)

    keep = "' :.,"
    to_remove = ''.join(ch for ch in string.punctuation if ch not in keep)
    ans = re.sub(f"[{re.escape(to_remove)}]", " ", ans)

    ans = re.sub(r"\s+", " ", ans).strip()

    return ans




