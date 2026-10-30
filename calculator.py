"""Простой калькулятор с основными арифметическими операциями."""


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


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculate(expression):
    """Вычисляет выражение вида '2 + 3'."""
    try:
        left, operator, right = expression.split()
        return OPERATIONS[operator](float(left), float(right))
    except KeyError:
        raise ValueError(f"Неизвестная операция: {operator}") from None


if __name__ == "__main__":
    print(calculate(input("Выражение (например, 2 + 3): ")))
