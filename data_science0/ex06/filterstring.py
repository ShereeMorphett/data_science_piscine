
import sys

from ft_filter import ft_filter


def main():
    """_summary_
    a program that accepts two arguments: a string(S), and an integer(N). The
    program should output a list of words from S that have a length
    greater than N.
    • Words are separated from each other by space characters.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        try:
            num = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        split_input = sys.argv[1].split()
        ft_result = [word for word in
                     ft_filter(lambda x: len(x) > num, split_input)]
        print(list(ft_result))

    except TypeError as msg:
        print(msg)
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main()
