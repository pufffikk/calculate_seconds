import pytest

from seconds import solution_2


@pytest.mark.parametrize(
    "time, expected",
    [
        ("01:00:01", 3601),
        ("00:00:00", 0),
        ("23:59:59", 86399)
    ]
)
def test_simple(time, expected):
    assert solution_2(time) == expected


@pytest.mark.parametrize(
    "time",
    [
        "",
        "smth",
        "24:01:01",
        "01:01:01:08",
        "01:01:01  Second",
        "01 :01 :01 :01",
        "01:01:01:05",
    ],
)
def test_error(time):
    with (pytest.raises(ValueError)):
        assert solution_2(time)

