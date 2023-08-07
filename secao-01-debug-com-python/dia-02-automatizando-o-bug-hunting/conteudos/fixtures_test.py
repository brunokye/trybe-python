import json
import os


def test_print_to_stdout(capsys):
    print("Hello, world!")
    captured = capsys.readouterr()

    assert captured.out == "Hello, world!\n"


def test_error_to_stderr(capsys):
    import sys

    sys.stderr.write("Error message\n")
    captured = capsys.readouterr()

    assert captured.err == "Error message\n"


def test_my_function(monkeypatch):
    from input import my_function

    def mock_input(_):
        return "Python"

    monkeypatch.setattr("builtins.input", mock_input)
    output = my_function()

    assert output == "Você digitou Python!"


def generate_output(content, path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(json.dumps(content))


def test_generate_output(tmp_path):
    content = {"a": 1}
    output_path = tmp_path / "out.json"

    generate_output(content, output_path)

    assert os.path.isfile(output_path)

    with open(output_path) as file:
        assert file.read() == '{"a": 1}'
