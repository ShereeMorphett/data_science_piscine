import numpy


def slice_me(family: list, start: int, end: int) -> list:
    new_array = numpy.array(family)
    print(f"My shape is: {new_array.shape}")
    split_array = new_array[start:end]
    print(f"My new shape is: {split_array.shape}")

    return (split_array.tolist())


def validate_data(to_slice: any):
    if type(to_slice) is list:
        raise ValueError("Lists are of different lengths")
    if not to_slice:
        raise ValueError("List is empty")
    previous_value = len(to_slice[0])
    for values in to_slice:
        if previous_value != len(values):
            raise ValueError("Lists values are of different lengths")


def main():
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    try:
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except ValueError as msg:
        print(msg)


if __name__ == "__main__":
    main()
