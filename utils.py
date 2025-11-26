import json
import base64


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


def clean_vqa_answer(answer: str):

    pass




