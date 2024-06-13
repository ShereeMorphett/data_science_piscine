# You must take in *args a quantity of unknown number and make the Mean, Median,
# Quartile (25% and 75%), Standard Deviation and Variance according to the **kwargs
# ask.
# You have to manage the errors.


# *args and **kwargs are special keyword which allows function to take variable length argument.

# mean : 95.6
# median : 42
# quartile : [11.0, 64.0]
# -----
# std : 17982.70124086944
# var : 323377543.9183673


"""Explanation of Each Function
quartiles(data):

Purpose: To calculate the first quartile (Q1) and third quartile (Q3) of the data.
Steps:
Sort the data: Arrange the data in ascending order.
Q1: Find the value at the 25th percentile.
Q3: Find the value at the 75th percentile.
Return: Q1 and Q3 values.
variance(data):

Purpose: To calculate the variance of the data, which measures the dispersion of the data points around the mean.
Steps:
Calculate the mean (mu): The average value of the data.
Sum of squared differences: Calculate the sum of the squared differences between each data point and the mean.
Divide by (n-1): Divide the sum by the number of data points minus one to get the sample variance.
Return: The variance of the data.
standard_deviation(data):

Purpose: To calculate the standard deviation, which is a measure of the amount of variation or dispersion in the data.
Steps:
Calculate variance: Compute the variance of the data.
Square root: Take the square root of the variance to get the standard deviation.
Return: The standard deviation of the data.
These functions are fundamental statistical tools used to summarize and understand the characteristics of a dataset."""

def mean(data):
    return sum(data) / len(data)

def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1, mid2 = sorted_data[n // 2 - 1], sorted_data[n // 2]
        return (mid1 + mid2) / 2

def quartiles(data):
    sorted_data = sorted(data)
    n = len(sorted_data)

    # Calculate the 25th percentile (Q1) using interpolation
    q1_position = 0.25 * (n - 1)
    q1 = interpolate(sorted_data, q1_position)
    
    # Calculate the 75th percentile (Q3) using interpolation
    q3_position = 0.75 * (n - 1)
    q3 = interpolate(sorted_data, q3_position)
    
    return q1, q3

def interpolate(sorted_data, position):
    lower_index = int(position)
    upper_index = min(lower_index + 1, len(sorted_data) - 1)
    weight = position - lower_index
    
    return sorted_data[lower_index] * (1 - weight) + sorted_data[upper_index] * weight

def variance(data):
    mu = mean(data)
    return sum((x - mu) ** 2 for x in data) / len(data)

def standard_deviation(data):
    return variance(data) ** 0.5

def ft_statistics(*args: any, **kwargs: any) -> None:
    data = [float(x) for x in args]  # Convert inputs to floats for calculations

    if not data:
        print("ERROR")
        return
    
    for key, value in kwargs.items():
        match value:
            case "mean":
                print(f"mean : {mean(data)}")
            case "median":
                print(f"median : {median(data)}")
            case "quartile":
                q1, q3 = quartiles(data)
                print(f"quartile : [{q1}, {q3}]")
            case "std":
                print(f"std : {standard_deviation(data)}")
            case "var":
                print(f"var : {variance(data)}")
            case _:
                print(f"Invalid request: {value}")

def main():
    try:
        ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
        print("-----")
        ft_statistics(toto="mean", tutu="median", tata="quartile")
    except Exception as e:
        print("ERROR", e)

if __name__ == "__main__":
    main()
