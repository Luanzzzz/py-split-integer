from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 20
    number_of_parts = 6
    result = split_integer(value, number_of_parts)
    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    results = split_integer(10, 5)
    assert len(set(results)) == 1


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 17
    result = split_integer(value, 1)
    assert result == [value]

def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result)

def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 5)
    assert result == [0, 0, 1, 1, 1]
