import pytest
def list_of_numbers(n: int) -> list:
    l = []
    for i in range (n):
        l.append(i + 1)
    return l

@pytest.mark.parametrize(
    'n, expected',
    [(1, [1]), (3, [1, 2, 3]), (5, [1, 2, 3, 4, 5])]
)
def test_list(n, expected):
    result = list_of_numbers(n)
    assert result == expected