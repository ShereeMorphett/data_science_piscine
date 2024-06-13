import matplotlib.pyplot as plt
from load_csv import load




def draw_graph(data, country):
    """
    Draw a graph for the specified country using the life expectancy data.
    Args:
    - data (DataFrame): The loaded data.
    - country (str): The name of the country to filter data for.
    """
    country_data = data[data["country"] == "Finland"]
    country_data = country_data.iloc[:,1:]

    country_data.index = [country]
    
    if country_data.empty:
        print(f"No data found for {country}")
        return

    country_data.T.plot()
    plt.title("Finland Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()




def main():
    """Main function to load data and draw graph for Finland."""
    try:
        # Load the data
        df = load("life_expectancy_years.csv")
        # Draw the graph for Finland
        draw_graph(df, "Finland")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
