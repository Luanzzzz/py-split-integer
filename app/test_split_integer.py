import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
"value, number_of_parts, expected_result",
[
    (8, 1, [8]),
        (6, 2, [3, 3]),
    (17, 4, [4, 4, 4, 5]),
    (32, 6, [5, 5, 5, 5, 6, 6]),
    (5, 5, [1, 1, 1, 1, 1]),
    (3, 5, [0, 0, 1, 1, 1]),
    (20, 5, [4, 4, 4, 4, 4]),
    (100, 7, [14, 14, 14, 14, 14, 15, 15]),
],
)

def test_split_integer_scenarios(value: int,
                            number_of_parts: int,
                            expected_result: list
                            ) -> None:
    result = split_integer(value, number_of_parts)

    assert result == expected_result
    assert len(result) == number_of_parts
    assert all(isinstance(item, int) for item in result)
    assert sum(result) == value
    if len(result) > 1:
        assert max(result) - min(result) <= 1
