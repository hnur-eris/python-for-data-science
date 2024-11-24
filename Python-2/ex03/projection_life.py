from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def data_control(gdp, life_exp):
    """
    This function checks the data control of the given datasets.
    """
    if len(gdp) != len(life_exp):
        print("The datasets have different lengths.")
        return False
    return True


def merge_datasets(gdp, life_exp):
    """
    This function merges the given datasets.
    """
    df = pd.merge(gdp, life_exp, on='country')
    df = df.dropna()
    return df.iloc[:, 1], df.iloc[:, 2]


def main():
    df1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df2 = load("life_expectancy_years.csv")

    if df1 is not None and df2 is not None:

        gdp = df1[['country', '1900']]
        life_exp = df2[['country', '1900']]
        # gdp.to_csv("gdp.csv") #looking for our dataset

        _gdp, _life_exp = merge_datasets(gdp, life_exp)

        if data_control(_gdp, _life_exp):
            plt.figure(figsize=(10, 6))
            plt.scatter(_gdp, _life_exp)
            plt.title('1900')
            plt.xscale("log")
            plt.xticks(ticks=[300, 1e3, 1e4], labels=['300', '1k', '10k'])
            plt.xlabel('Gross domestic product')
            plt.ylabel('Life Expectancy')

            try:
                plt.show()
            except (Exception, KeyboardInterrupt) as e:
                print(f"Error: {e}")
                exit(0)


if __name__ == "__main__":
    main()
