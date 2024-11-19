from load_csv import load
import matplotlib.pyplot as plt

def main():
    dataset1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    dataset2 = load("life_expectancy_years.csv")
    
    if dataset1 is not None and dataset2 is not None:
        
        gdp = dataset1[['country', '1900']]
        life_exp = dataset2[['country','1900']]
        merge = gdp.merge(life_exp, on='country', suffixes=['_gdp', '_life'])
        
        
        plt.plot(merge['1900_gdp'], merge['1900_life'], 'o')
        plt.title('1900')
        plt.xticks(ticks=[300, 1e3, 1e6], labels=['300', '1k', '10k'])
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')
        plt.show()


if __name__ == "__main__":
    main()