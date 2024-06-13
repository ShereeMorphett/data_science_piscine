import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def update_values(data: pd.DataFrame) -> pd.DataFrame:

    for col in data.columns:
        data[col] = data[col].replace({'M': 'e+6', 'B': 'e+9', 'k': 'e+3'}, regex=True).astype(float).astype(int)
    print(data)
    return data


def draw_graph(data: pd.DataFrame, country: str, other_country : str):
    """
    Draw a graph for the specified country using the life expectancy data.
    Args:
    - data (DataFrame): The loaded data.
    - country (str): The name of the country to filter data for.
    """
    
    country_data = data[data["country"] == country]
    other_country_data = data[data["country"] == other_country]
    country_data = country_data.iloc[:,1:]
    other_country_data = other_country_data.iloc[:,1:]
    country_data.index = [country]
    other_country_data.index = [other_country]
    print(country_data)
    
    country_data = update_values(country_data)
    other_country_data = update_values(other_country_data)
    
    if country_data.empty:
        print(f"No data found for {country}")
        return
    fin_data = country_data.T.plot(color=['Pink'])
    other_country_data.T.plot(ax=fin_data, color=['Green'])
    
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.show()




def main():
    """Main function to load data and draw graph for Finland."""
    try:
        # Load the data
        df = load("population_total.csv")
        # Draw the graph for Finland
        draw_graph(df, "Finland", "Australia")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
