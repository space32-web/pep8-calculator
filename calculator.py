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


def square_root(a):
    """Возвращает квадратный корень из a; для a < 0 — ValueError."""
    if a < 0:
        raise ValueError("Корень из отрицательного числа не определён")
    return math.sqrt(a)


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide,
              "^": power}


def calculate(expression):
    """Вычисляет выражение вида '2 + 3' или 'sqrt 16'."""
    parts = expression.split()
    if len(parts) == 2 and parts[0] == "sqrt":
        return square_root(float(parts[1]))
    if len(parts) != 3:
        raise ValueError("Формат выражения: число операция число")
    left, operator, right = parts
    if operator not in OPERATIONS:
        raise ValueError(f"Неизвестная операция: {operator}")
    return OPERATIONS[operator](float(left), float(right))


def main():
    """Читает выражение и выводит результат или сообщение об ошибке."""
    try:
        print(calculate(input("Выражение (например, 2 + 3): ")))
    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
