import pandas as pd
import matplotlib.pyplot as plt

raw_housing_data=pd.read_csv("housing_prices.csv")
#boxplot graph
plt.boxplot(raw_housing_data["Age of House (in Years)"])

