import pandas as pd
import matplotlib.pyplot as plt

raw_housing_data=pd.read_csv("housing_prices.csv")
#histogram graph
plt.hist(raw_housing_data["Sale Price"], bins=10)