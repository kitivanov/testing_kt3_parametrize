def is_even(number):
    """Проверяет, является ли число четным"""
    return number % 2 == 0


def calculate_area(length, width):
    """вычисляет площадь прямоугольника"""
    if length < 0 or width < 0:
        raise Exception("Length and width must be non-negative")
    return length * width


def classify_triangle(a, b, c):
    """Принимает длины трех сторон треугольника и возвращает тип треугольника"""
    if a <= 0 or b <= 0 or c <= 0:
        raise Exception("Sides must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise Exception("Triangle inequality violated")

    if a == b == c:
        return "равносторонний"
    elif a == b or b == c or a == c:
        return "равнобедренный"
    else:
        return "разносторонний"
