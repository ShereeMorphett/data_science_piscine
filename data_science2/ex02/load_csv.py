import pandas as pd

# Make a function that takes a path as argument, writes the dimensions of the data set
# and returns it. You have to handle the error cases and return None if the path is bad,
# bad format..


def load(path: str) -> pd.DataFrame:
    """_summary_
    writes the dimensions of the data set and returns it

    Args:
        path (str): FilePath

    Returns:
        pd.DataFrame: returns the read DataFrame
    """

    try:
        if path.endswith('.csv'):
            df = pd.read_csv(path)
            if df.empty:
                print('CSV file is empty')
            else:
                print(f"Loading dataset of dimensions {df.shape}")
                return df
        else:
            raise TypeError("Invalid file extension")
    except Exception as e:
        print(f"Error: {e}")
        return None
    return df


def main():
    """_summary_
        This is a main, it simply calls load
    """
    try:
        print(load("life_expectancy_years.csv"))
        print(load("load_csv.py"))
        print(load("this.csv"))
    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    main()
