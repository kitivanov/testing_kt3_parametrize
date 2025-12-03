import pytest
from src.main import is_even, calculate_area, classify_triangle


@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True),
    (-5, False),
])
def test_is_even(number, expected):
    assert is_even(number) == expected


@pytest.mark.parametrize("length, width, expected", [
    (2, 3, 6),
    (0, 5, 0),
    (4.5, 2, 9.0),
])
def test_calculate_area(length, width, expected):
    assert calculate_area(length, width) == expected


@pytest.mark.parametrize("length, width", [
    (-1, 2),
    (3, -5),
])
def test_calculate_area_invalid(length, width):
    with pytest.raises(Exception):
        calculate_area(length, width)


@pytest.mark.parametrize("a, b, c, expected", [
    (3, 3, 3, "равносторонний"),
    (3, 3, 2, "равнобедренный"),
    (3, 4, 5, "разносторонний"),
])
def test_classify_triangle(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected


@pytest.mark.parametrize("a, b, c", [
    (0, 3, 4),
    (1, 2, 3),
    (-3, 4, 5),
])
def test_classify_triangle_invalid(a, b, c):
    with pytest.raises(Exception):
        classify_triangle(a, b, c)
