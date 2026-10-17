import logging
import re

from curlify import to_curl


class RequestUtils:
    """Базовий клас для виконання HTTP-запитів."""

    logger = logging.getLogger(__name__)

    def __init__(self, session):
        # Зберігаємо сесію для повторного використання з'єднання та заголовків.
        self.session = session

    def send_request(
        self,
        method,
        path,
        params=None,
        json=None,
        headers=None,
        auth=None,
        expected_status_code=None,
    ):
        # Фіксуємо початок запиту та його query-параметри.
        self.logger.info("Sending request to %s with params=%s", path, params)

        # Виконуємо запит відповідним HTTP-методом.
        if method.upper() == "GET":
            response = self.session.get(
                path,
                params=params,
                headers=headers,
            )
        elif method.upper() == "POST":
            response = self.session.post(
                path,
                auth=auth,
                json=json,
                headers=headers,
            )
        else:
            raise ValueError(f"Method {method} not supported")

        # Формуємо cURL-представлення запиту для діагностики.
        curl_ = to_curl(response.request)

        # Маскуємо Bearer-токен перед записом запиту в лог.
        curl_ = re.sub(
            r"(-H\s+['\"]Authorization:\s*Bearer\s+)[^'\"]*(['\"])",
            r"\1***\2",
            curl_,
            flags=re.IGNORECASE,
        )

        # Видаляємо заголовок Basic Auth із cURL-логу повністю.
        curl_ = re.sub(
            r"\s*-H\s+['\"]Authorization:\s*Basic\s+[^'\"]*['\"]",
            "",
            curl_,
            flags=re.IGNORECASE,
        )

        self.logger.info("CURL: %s", curl_)
        self.logger.info("Response status code: %s", response.status_code)

        # За потреби перевіряємо очікуваний HTTP-статус.
        if expected_status_code is not None:
            assert response.status_code == expected_status_code, (
                f"Expected status code {expected_status_code}, "
                f"but received {response.status_code}"
            )

        return response