
def give_bmi(height: list[int | float], weight: list[int | float]) -> \
        list[int | float]:
    """calculates bmi from height and weight values and matching index

    Returns:
        list[int | float]: calculated bmi
    """
    index = 0
    bmi_list = []
    while index < len(height) and index < len(height):
        bmi_list.append(weight[index]/(height[index] ** 2))
        index += 1
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """_summary_

    Args:
        bmi (list[int  |  float]): List of bmi
        limit (int): max bmi rate

    Returns:
        list[bool]: True if the value in bmi at same index is greater than
        the limit
    """
    limit_bool = []
    for value in bmi:
        limit_bool.append(limit < value)
    return limit_bool


def validate_data(height: list[int | float], weight: list[int | float]):
    """_summary_
    Validates the data in height and weight to ensure same length and correct
    value
    Args:
        height (list[int  |  float]): Height of person in cm
        weight (list[int  |  float]): Weight of person in kg

    Raises:
        AssertionError: The lists are incorrect lengths
        ValueError: The values in one of the lists are not flt/int
    """
    if len(height) != len(weight):
        raise AssertionError("Lists are of different lengths")
    index = 0
    while index < len(height) and index < len(weight):
        if type(height[index]) is not int and type(height[index]) is not \
            float or type(height[index]) is not int and type(height[index]) \
                is not float:
            raise ValueError("Lists values are not int/float")
        index += 1


def main():
    """
    _summary_
    this is a main that does validations
    """
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    try:
        validate_data(height, weight)
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except AssertionError as msg:
        print(msg)
    except ValueError as msg:
        print(msg)


if __name__ == "__main__":
    main()
