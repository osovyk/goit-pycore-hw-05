import re

from collections.abc import Callable


def generator_numbers(text: str) -> float:
    if type(text) is not str:
        raise TypeError("The input must be string")

    pattern = r'-?\d+\.?\d*'
    matches = re.findall(pattern, text)

    for match in matches:
        yield float(match)


def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))
