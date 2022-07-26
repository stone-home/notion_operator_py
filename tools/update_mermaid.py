# -*- coding: utf-8 -*-
# @Filename : update_mermaid
# @Date : 2022-07-26-15-59
# @Project: nt-integration-sdk

import base64
import requests
import io
import os
from PIL import Image


def fetch_workspace():
    current_path = os.path.abspath(__file__)
    workspace = os.path.dirname(os.path.dirname(current_path))
    return workspace


def generate_mermaid_image(mmd_file: str, output: str):
    with open(mmd_file, 'rb') as fb:
        graph = fb.read()
    base64_bytes = base64.b64encode(graph)
    base64_string = base64_bytes.decode("ascii")
    img = Image.open(io.BytesIO(requests.get('https://mermaid.ink/img/' + base64_string).content))
    with open(output, "wb") as fb:
        img.save(fb)


def list_mmd_file(dir_path: str):
    mmd_list = []
    for element in os.listdir(dir_path):
        file_path = os.path.join(dir_path, element)
        if os.path.splitext(element)[-1] == '.mmd' and os.path.isfile(file_path):
            mmd_list.append(file_path)
    return mmd_list


def transfer2image(mmd_file: str, output: str):
    try:
        generate_mermaid_image(mmd_file, output)
    except Exception:
        print(f"Transfer Failed for mmd file: {mmd_file}")
    else:
        print(f"mermaid PNG image transfer success, {output}")


if __name__ == '__main__':
    mmd_dir = os.path.join(fetch_workspace(), 'docs/assets/mermaid_images')
    mmd_list = list_mmd_file(mmd_dir)
    for element in mmd_list:
        output_file = f"{element}.png"
        transfer2image(element, output_file)