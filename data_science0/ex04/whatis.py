import sys

try:
    argc = len(sys.argv)
    assert argc <= 2, "more than one argument is provided"
    assert argc == 2

    try:
        num = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as msg:
    print(msg)
