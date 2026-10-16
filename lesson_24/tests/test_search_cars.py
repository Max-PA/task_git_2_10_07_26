import logging

import pytest
from lesson_24.core.api.car_service.controller import CarsController

logger = logging.getLogger(__name__)


class TestGetCars:

    @pytest.fixture(scope="class")
    def cars_controller(self):
        # Створюємо контролер і виконуємо авторизацію один раз
        # для всіх тестів цього класу.
        logger.info("Initializing CarsController and authenticating")

        controller = CarsController()
        controller.dz_auth()

        yield controller

        # Закриваємо HTTP-сесію після завершення всіх тестів класу.
        controller.session.close()
        logger.info("HTTP session closed")

    def test_get_all_cars(self, cars_controller):
        logger.info("Starting test: get all cars")

        list_of_cars = cars_controller.get_search_cars()

        # Перевіряємо, що API повернув список із 25 автомобілів.
        assert isinstance(list_of_cars, list), \
            "API response must be a list of cars"
        assert len(list_of_cars) == 25, \
            f"Expected 25 cars but received {len(list_of_cars)}"

        logger.info("Test passed: received all 25 cars")

    def test_search_cars_by_price(self, cars_controller):
        logger.info("Starting test: sort cars by price")

        list_of_cars = cars_controller.get_search_cars(
            query_parameters={"sort_by": "price"}
        )

        # Переконуємося, що API повернув список автомобілів.
        assert isinstance(list_of_cars, list), \
            "API response must be a list of cars"

        # Перевіряємо сортування цін за зростанням.
        prices = [car["price"] for car in list_of_cars]
        assert prices == sorted(prices), \
            "Cars are not sorted by price in ascending order"

        logger.info("Test passed: cars are sorted by price")

    def test_search_cars_with_limit(self, cars_controller):
        logger.info("Starting test: limit cars to 5")

        list_of_cars_with_limit_5 = cars_controller.get_search_cars(
            query_parameters={"limit": 5}
        )

        # Перевіряємо тип відповіді перед перевіркою її вмісту.
        assert isinstance(list_of_cars_with_limit_5, list), \
            "API response must be a list of cars"

        # Перевіряємо, що параметр limit обмежив відповідь п'ятьма автомобілями.
        assert len(list_of_cars_with_limit_5) == 5, \
            f"Expected 5 cars but received {len(list_of_cars_with_limit_5)}"

        logger.info("Test passed: received 5 cars")

    # Перевіряємо сортування та limit для різних комбінацій параметрів.
    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 7),
        ("brand", 10),
        ("price", None),
        (None, 5),
        (None, None)
    ])
    def test_cars_sort_by_check(self, cars_controller, sort_by, limit):
        logger.info(
            "Starting test: sort_by=%s, limit=%s",
            sort_by,
            limit
        )

        # Передаємо до API лише параметри, для яких задано значення.
        query_parameters = {
            key: value
            for key, value in {"sort_by": sort_by, "limit": limit}.items()
            if value is not None
        }

        cars_sorted = cars_controller.get_search_cars(
            query_parameters=query_parameters
        )

        # Враховуємо стандартне сортування API за brand,
        # якщо параметр sort_by не передано.
        sort_field = sort_by if sort_by is not None else "brand"
        values = [car[sort_field] for car in cars_sorted]

        assert values == sorted(values), \
            f"The data is not sorted by field {sort_field}"

        # Якщо limit не задано, API має повернути всі 25 автомобілів.
        expected_count_of_items = limit if limit is not None else 25

        assert len(cars_sorted) == expected_count_of_items, (
            f"Expected {expected_count_of_items} cars, "
            f"received {len(cars_sorted)}"
        )

        logger.info(
            "Test passed: sort_by=%s, limit=%s, received=%s cars",
            sort_field,
            limit,
            len(cars_sorted)
        )