import pytest

from src.hex_converter import hexadecimal_to_decimal

pytestmark = pytest.mark.dependency


@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ("8", 8),
        ("9", 9),
        ("a", 10),
        ("b", 11),
        ("c", 12),
        ("e", 14),
        ("f", 15),
    ],
)
def test_converter(input_string, expected_result):
    assert hexadecimal_to_decimal(input_string) == expected_result
