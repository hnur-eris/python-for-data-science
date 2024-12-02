import matplotlib.pyplot as plt
from load_csv import load


def str_to_int(value: str) -> int:
    """
    Convert a population string like '1.27M' or '900K' to an integer.

    Parameters:
    ----------
    value : str
        String containing a number with 'M' (millions) or 'K' (thousands).

    Returns:
    ----------
    int
        The converted integer value.
    """
    if 'M' in value:
        numeric_value = float(value.replace('M', ''))
        return int(numeric_value * 1_000_000)
    elif 'K' in value:
        numeric_value = float(value.replace('K', ''))
        return int(numeric_value * 1_000)
    else:
        return int(value)


def process_popu(dataset, country):
    """
        This function gives the population values for a given country
    """
    if dataset is not None:
        data = dataset[dataset["country"] == country]
        years = data.columns[1:]
        f_campus = [str_to_int(val) for val in data.values[0][1:]]
        plt.plot(years, f_campus, label=f"Population of {country}")
        plt.xticks(years[::40])


def main():
    """
        Loads the population dataset,
        filters the data for France and Turkey,
        and plots the population over the years
    """
    dataset = load("population_total.csv")

    process_popu(dataset, "France")
    process_popu(dataset, "Turkey")

    plt.xlabel("Year")
    plt.ylabel("Population")

    plt.title("Population Projections")

    ticks = [0, 2e7, 4e7, 6e7]
    plt.yticks(ticks, ['0', '20M', '40M', '60M'])

    plt.legend()

    try:
        plt.show()
    except (Exception, KeyboardInterrupt) as e:
        print(f"Error: {e}")
        exit(0)


if __name__ == "__main__":
    main()
