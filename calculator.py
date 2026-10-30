"""Простой калькулятор с основными арифметическими операциями."""
import math


def add(a, b):
    """Возвращает сумму a и b."""
    return a + b


def subtract(a, b):
    """Возвращает разность a и b."""
    return a - b


def multiply(a, b):
    """Возвращает произведение a и b."""
    return a * b


def divide(a, b):
    """Возвращает частное a и b; при b == 0 выбрасывает ValueError."""
    if b == 0:
        raise ValueError("Деление на ноль")
    return a / b


def power(a, b):
    """Возвращает a в степени b."""
    return a ** b


def square_root(a, _=None):
    """Возвращает квадратный корень из a."""
    return math.sqrt(a)


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide,
              "^": power}


def calculate(expression):
    """Вычисляет выражение вида '2 + 3' или 'sqrt 16'."""
    parts = expression.split()
    if len(parts) == 2 and parts[0] == "sqrt":
        return square_root(float(parts[1]))
    try:
        left, operator, right = parts
        return OPERATIONS[operator](float(left), float(right))
    except KeyError:
        raise ValueError(f"Неизвестная операция: {operator}") from None


if __name__ == "__main__":
    print(calculate(input("Выражение (например, 2 + 3): ")))
