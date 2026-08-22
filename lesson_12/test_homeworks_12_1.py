from assertpy import soft_assertions, assert_that

from homeworks import sum_of_numbers_in_array
from homeworks import Employee, Manager, Developer, TeamLead
import pytest

@pytest.mark.parametrize(
        'input_data, expected_result',
        [
            ("1,2,3,4", 10), # позитивний тест
            ("1,2,3,4,50", 60), # позитивний тест, більша кількість значень
            ("0", 0), # нуль
            ("1,-2,3", 2), # додатні та від'ємні числа
            ("-1,-2,-3", -6) # від'ємна сума
        ])

# test 1 - 6 --- Тестування поведінки функції sum_of_numbers_in_array()
def test_sum_of_numbers_returns_correct_result(input_data, expected_result):
    actual_result = sum_of_numbers_in_array(input_data)
    assert actual_result == expected_result, (f"Sum of numbers in array should "
                                              f"be {expected_result} but it is {actual_result}")


# Перевірка обробки некоректного input
def test_return_of_none_for_incorrect_string_input():
    actual_result = sum_of_numbers_in_array("qwerty1,2,3")
    expected_result = None
    assert actual_result == expected_result, (f"Sum of numbers in array should "
                                              f"be {expected_result} but it is {actual_result}")


# Перевіряємо результат обчислення на прикладі порожнього рядку.
def test_return_of_none_for_empty_input():
    actual_result = sum_of_numbers_in_array("")
    expected_result = None
    assert actual_result == expected_result, (f"Sum of numbers in array should "
                                              f"be {expected_result} but it is {actual_result}")


# Перевірка великої кількості вхідних даних
def test_sum_of_a_range_of_numbers_returns_correct_result():
    actual_result = sum_of_numbers_in_array(",".join(str(number) for number in range(1, 1001)))
    expected_result = sum(range(1, 1001))
    assert actual_result == expected_result, (f"Sum of numbers in array should "
                                              f"be {expected_result} but it is {actual_result}")

# Тест на великих числах
def test_sum_of_large_numbers_returns_correct_result():
    actual_result = sum_of_numbers_in_array("1000000000,2000000000,3000000000")
    expected_result = 6000000000
    assert actual_result == expected_result, (f"Sum of numbers in array should "
                                              f"be {expected_result} but it is {actual_result}")


# Повернення None у разі надходження input з порожніми даними напр.: "1,,3"
def test_return_of_none_for_empty_element_between_separators():
    actual_result = sum_of_numbers_in_array("1,,3") # некоректний input
    expected_result = None
    assert actual_result == expected_result, (f"Sum of numbers in array should "
                                              f"be {expected_result} but it is {actual_result}")


# Тестування об'єктів, атрибутів та значень атрибутів класів: Employee, Manager, Developer, TeamLead
# Перевіряємо наявність обов'язкових атрибутів Employee
def test_employee_has_required_attributes():
    employee = Employee("John", 5000)

    assert hasattr(employee, "name")
    assert hasattr(employee, "salary")

# Перевіряємо значення атрибутів Employee
def test_employee_has_correct_attribute_values():
    employee = Employee("John", 5000)

    assert employee.name == "John"
    assert employee.salary == 5000

# тестуємо чи class Manager має власний атрибут department
def test_manager_has_his_own_required_attribute():
    manager = Manager(department="Sales",
                      name="Mike",
                      salary=7000
                      )

    assert hasattr(manager, "department")

# Перевіряємо успадковані атрибути Employee
def test_manager_has_employee_required_attribute_value():
    manager = Manager(department="Sales",
                      name="Mike",
                      salary=7000
                      )

    assert hasattr(manager, "name")
    assert hasattr(manager, "salary")


# Перевіряємо коректність значень  усіх атрибутів та їх очікувані значення
def test_manager_has_correct_attribute_values():
    manager = Manager(department="Sales",
                      name="Mike",
                      salary=7000
                      )

    assert manager.department == "Sales"
    assert manager.name == "Mike"
    assert manager.salary == 7000


# Перевіряємо власний атрибут Developer
def test_developer_has_his_own_required_attribute_value():
    developer = Developer(programming_language="C#",
                          name="Max",
                          salary=10000
                          )

    assert hasattr(developer, "programming_language")


# Перевіряємо успадковані атрибути Employee
def test_developer_has_employee_required_attribute_value():
    developer = Developer(programming_language="C#",
                          name="Max",
                          salary=10000
                          )

    assert hasattr(developer, "name")
    assert hasattr(developer, "salary")


# Перевіряємо значення атрибутів Developer
def test_developer_has_correct_attributes_values():
    developer = Developer(
        programming_language="C#",
        name="Max",
        salary=10000
    )

    assert developer.programming_language == "C#"
    assert developer.name == "Max"
    assert developer.salary == 10000


# Перевіряємо коректність значень усіх атрибутів та їх очікувані значення

def test_teamlead_has_correct_attributes_values():
    teamlead = TeamLead(
            programming_language="Python",
            department="Development",
            name="John",
            salary=5000,
            team_size=10
            )
    with soft_assertions():

        assert_that(teamlead.programming_language, "TeamLead programming_language").is_equal_to("Python")
        assert_that(teamlead.department, "TeamLead department").is_equal_to("Development")
        assert_that(teamlead.name, "TeamLead name").is_equal_to("John")
        assert_that(teamlead.salary, "TeamLead salary").is_equal_to(5000)
        assert_that(teamlead.team_size, "TeamLead team_size").is_equal_to(10)

# test 16 - 17 --- Тестування структуру inheritance та MRO
# Перевіряємо  успадкування між класами
def test_inheritance_from_class_employee_in_class_manager():

    assert Employee in Manager.__mro__
    assert Employee in Developer.__mro__
    assert Employee in TeamLead.__mro__
    assert Manager in TeamLead.__mro__
    assert Developer in TeamLead.__mro__


# Перевіряємо порядок класів при ромбовидному наслідуванні для класу TeamLead
def test_order_of_the_mro_in_class_teamlead():
    actual_result = TeamLead.__mro__
    expected_result = (TeamLead, Manager, Developer, Employee, object)
    assert actual_result == expected_result, (f"The order of the __mro__ in class should "
                                              f"be {expected_result} but it is {actual_result}")