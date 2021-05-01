import pandas as pd
import matplotlib.pyplot as plt
"""
raw_housing_data=pd.read_csv("housing_prices.csv")
#scatter graph
plt.scatter(x=raw_housing_data["Flat Area (in Sqft)"], 
            y=raw_housing_data["Sale Price"], 
            color="Red")
plt.xlabel("Flat Area (in Sqft)")
plt.ylabel("Sale Price")
plt.title("Selling price Vs Area")
"""

plotdata = pd.DataFrame({
    
    "Demand":[243, 265, 290, 326, 378, 409, 438, 465, 490, 516, 545, 571, 598, 626, 654, 684, 714, 746],
    "Supply":[146, 167, 196, 244, 300, 367, 384, 389, 394, 400, 431, 437, 442, 448, 454, 461, 467, 471]
    }, 
    index=["2012-13", "2013-14", "2014-15", "2015-16", "2016-17", "2017-18", "2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26", "2026-27", "2027-28", "2028-29", "2029-30"]
)
plotdata.plot(kind="bar", color={"Demand": "#FF00FF", "Supply": "#00FF00"})
plt.title("Demand-Supply capacity from 2012-13 to 2029-30")
#plt.xlabel("")
plt.ylabel("Quantity of Gas (MMSCMD)")





