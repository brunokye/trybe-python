import pytest

from src.hex_converter import (
    main,
    print_hexadecimal_to_decimal,
    write_hexadecimal_to_decimal,
)

pytestmark = pytest.mark.dependency


def test_monkeypatch(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "a")
    assert main() == 10


def test_capsys(capsys):
    print_hexadecimal_to_decimal("a")
    captured = capsys.readouterr()
    assert captured.out == "10\n"
    assert captured.err == ""


def test_tmp_path(tmp_path):
    output_file = tmp_path / "output.txt"
    write_hexadecimal_to_decimal("a", output_file)
    assert output_file.read_text() == "10"
