from homework_18_2 import post_request, get_request, delete_request
import pytest
import requests

filename = 'candle.avif'

def test_post_get_delete_request():
    post_response = post_request()
    post_response_json = post_response.json()
    post_request_image_url = post_response_json['image_url']
    assert post_response.status_code == 201
    assert isinstance(post_request_image_url, str)
    assert post_request_image_url.startswith("http://127.0.0.1:8080/")
    assert post_request_image_url.endswith(filename)

    get_response = get_request(filename)
    assert get_response.status_code == 200

    get_response_json = get_response.json()
    get_request_image_url = get_response_json['image_url']

    assert isinstance(get_request_image_url, str)
    assert get_request_image_url.startswith("http://127.0.0.1:8080/")
    assert get_request_image_url.endswith(filename)

    delete_response = delete_request(filename)
    assert delete_response.status_code == 200


def test_get_request_after_delete_req():

    with pytest.raises(requests.exceptions.HTTPError, match="404 Client Error"):
        get_request(filename)