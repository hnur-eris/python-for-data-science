from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
        Loads the life expectancy dataset,
        filters the data for Turkey,
        and plots the life expectancy over the years.
    """
    dataset = load("life_expectancy_years.csv")
    if dataset is not None:
        data = dataset[dataset['country'] == 'Turkey']
        years = data.columns[1:]
        life_expectancy = data.values[0][1:]
        plt.plot(years, life_expectancy)
        plt.title('Life Expectancy in Turkey Over the Years')
        plt.xlabel('Year')
        plt.xticks(years[::40])
        plt.ylabel('Life Expectancy')
        try:
            plt.show()
        except (Exception, KeyboardInterrupt) as e:
            print(f"Error: {e}")
            exit(0)


if __name__ == "__main__":
    main()
