import pytest

from seconds import solution_2


def test_simple():
    assert solution_2("01:00:01") == 3601


def test_zero():
    assert solution_2("00:00:00") == 0


def test_maximum():
    assert solution_2("23:59:59") == 86399


def test_error():
    with (pytest.raises(ValueError)):
        assert solution_2("24:00:01")

