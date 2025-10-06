from typing import  Any

def assert_status_code(actual:int, expected: int):
    """
    Проверяет, что фактический статус - кодответа соответствует ожидаемому.
    :param actual: Фактический статус - код ответа.
    :param expected: Ожидаемый статус - код.
    :raises AssertionError: Если статус - коды не совпадают.
    """
    assert actual == expected, (
        'Incorrect response from server. '
        f'Expected status code {expected},'
        f'Actual status code {actual}'
    )



def assert_equal(actual: Any, expected: Any, name: str):
    """
    проверяет, что фактическое отображение равно проверяемому
    :param actual: Фактический значение.
    :param expected: Ожидаемое значение.
    :raises AssertionError: Если фактическое и актуальное не совпадает.
    """
    assert actual == expected, (
        f'Incorrect value: "{name}".'
        f'Expected value "{expected}"'
        f'Actual value "{actual}"'
    )