import logging

import requests
from requests.auth import HTTPBasicAuth

from lesson_24.core.utils.request_utils import RequestUtils
from lesson_24.core.utils.settings import d_settings


class CarsController(RequestUtils):
    """Контролер для роботи з endpoint /auth та /cars."""

    def __init__(self, base_url=d_settings.CARS_URL):
        self.auth_value = None
        self.base_url = base_url
        self.session = requests.Session()

        # Передаємо сесію базовому класу для виконання HTTP-запитів.
        super().__init__(self.session)

    def dz_auth(self, expected_status_code=200):
        response = self.send_request(
            method="POST",
            path=f"{self.base_url}/auth",
            auth=HTTPBasicAuth(d_settings.USER_NAME, d_settings.USER_PWD),
            expected_status_code=expected_status_code,
        )

        # Зберігаємо JWT і додаємо його до наступних запитів.
        auth_token = response.json()
        self.auth_value = auth_token["access_token"]
        self.session.headers.update(
            {"Authorization": f"Bearer {self.auth_value}"}
        )

        return self.auth_value

    def get_search_cars(
        self,
        query_parameters=None,
        expected_status_code=200,
    ):
        response = self.send_request(
            method="GET",
            path=f"{self.base_url}/cars",
            params=query_parameters,
            expected_status_code=expected_status_code,
        )

        return response.json()