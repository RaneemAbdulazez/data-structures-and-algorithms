from challenges.array_binary_search import __version__

from challenges.array_binary_search.array_binary_search import binary_search


def test_version():
    assert __version__ == "0.1.0"


def test_exist_key():
    expected = 2
    actual = binary_search([4, 8, 15, 16, 23, 42], 15)
    assert actual == expected


def test_not_exist_key():
    expected = -1
    actual = binary_search([11, 22, 33, 44, 55, 66, 77], 90)
    assert actual == expected


def test_not_exist_key2():
    expected = -1
    actual = binary_search([1, 2, 3, 5, 6, 7], 4)
    assert actual == expected
