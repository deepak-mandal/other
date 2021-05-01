import pandas as pd
import matplotlib.pyplot as plt

raw_housing_data=pd.read_csv("housing_prices.csv")
#line graph
#plt.plot(raw_housing_data["Sale Price"], color="Violet")
plt.plot(raw_housing_data["Sale Price"], marker="o", markerfacecolor="Blue", markersize=5, color="Green", linewidth=5, linestyle="dashed")
plt.xlabel("No. of records")
plt.ylabel("Sale Price")
plt.title("My first graphs (line graph)")
#plt.show()


