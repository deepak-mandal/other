import pandas as pd
import matplotlib.pyplot as plt
raw_housing_data=pd.read_csv("housing_prices.csv")
# to find the count of records across the different unique value of the condition of the house
raw_housing_data.groupby("Condition of the House")["ID"].count()
values=[30, 1701, 14031, 5679, 172]
labels=["Bad", "Excellent", "Fair", "Good", "Okay"]

#Bar graphs
plt.bar(labels, values, color="Blue", linewidth=5, linestyle="dashed")
plt.xlabel("The condition of the house")
plt.ylabel("Count of the Houses")
plt.title("Bar Graphs of housing_prices.csv data")

