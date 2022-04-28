import requests
import json
from pprint import pprint


with open('token_ya.txt', 'r') as f:
    token_ya = f.read().strip()


def get_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token_ya}'
    }


def get_folders_files_list():
    folders_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    params = {
        'path': 'disk:/'
    }
    headers = get_headers()
    response = requests.get(folders_url, params=params, headers=headers, timeout=5)
    return response.status_code, response.json()


def new_folder():
    folder_name = input('name: ')
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = get_headers()
    params = {'path': folder_name}
    response = requests.put(upload_url, headers=headers, params=params)
    return response.status_code  # 201 or 409 if already exists


if __name__ == "__main__":
    new_folder()
