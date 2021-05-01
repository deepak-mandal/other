import pandas as pd
import matplotlib.pyplot as plt

raw_housing_data=pd.read_csv("housing_prices.csv")
#histogram graph
plt.hist(raw_housing_data["Age of House (in Years)"], bins=10)
plt.xlabel("Age of House (in Years)")
plt.ylabel("No. of Records")
plt.title("Age wise distribution of houses")

