import pytest
from give_bmi import give_bmi, apply_limit, validate_data

height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

def test_give_bmi():
   height = [2.71, 1.15]
   weight = [165.3, 38.4]
   expected_output =  [22.507863455018317, 29.0359168241966]
   bmi = give_bmi(height, weight)
   assert bmi == expected_output


def test_apply_limit():
   bmi =  [22.507863455018317, 29.0359168241966]
   limits_output = apply_limit(bmi, 26)
   print(limits_output)
   expected_output = [False, True]
   assert limits_output == expected_output


def test_data_validation_value():
    height = [2.71, "additiong"]
    weight = [165.3, 38.4]
    with pytest.raises(ValueError) as excinfo:
        validate_data(height, weight)
    assert str(excinfo.value) == "Lists values are not int/float"


def test_data_validation_length():
    height = [2.71, 1.15]
    weight = [165.3, 38.4, 100.4647373]
    with pytest.raises(AssertionError) as excinfo:
        validate_data(height, weight)
    assert str(excinfo.value) == "Lists are of different lengths"
