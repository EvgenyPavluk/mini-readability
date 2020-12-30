import pytest
from formatter import Formatter


config = {
    "max_length": 20,
    "h1": {
      "bottom": 1
    },
    "p": {
      "bottom": 1
    }
}

formatter = Formatter(config)


def test_empty_data():
    assert formatter([]) == []


def test_empty_line():
    assert formatter.format_line('p', '') == ''


def test_simple():
    formatted = formatter.format_line('p', 'aa ' * 10)
    assert formatted == (
        'aa aa aa aa aa aa \n'
        'aa aa aa aa \n\n'
    )
