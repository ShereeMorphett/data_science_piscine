
def NULL_not_found(object) -> int:
    null_types = {
        'Nothing': None,
        'Garlic': float('NaN'),
        'Zero': 0,
        'Empty': '',
        'Fake': False
    }

    for name, value in null_types.items():
        if object is value or (isinstance(object, float) and
           isinstance(value, float) and str(object) == str(value)):
            print(f"{name}: {value} {type(object)}")
            return 0
    print("Type not Found")
    return 1
