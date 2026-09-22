# ДЗ 18.2.POST / GET / DELETE
import requests

BASIC_ADDRESS = "http://127.0.0.1:8080"
filename = 'candle.avif'

def post_request():
    with open(filename, 'rb') as file:
        files = {'image': file}
        response = requests.post(f'{BASIC_ADDRESS}/upload', files=files)
        response.raise_for_status()
    return response


def get_request(filename):
    response = requests.get(
        f'{BASIC_ADDRESS}/image/{filename}',
        headers={"Content-Type": "text"}
    )
    response.raise_for_status()
    return response


def delete_request(filename):
    response = requests.delete(f"{BASIC_ADDRESS}/delete/{filename}")
    response.raise_for_status()
    return response