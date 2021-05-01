#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 01:50:54 2021

@author: deepak
"""
#Machine Learning
#Pie chart in Python with legends:
import matplotlib.pyplot as plt
values = [158.88, 96.85, 22.32, 27.00, 65.01, 8.00]
colors = ['b', 'g', 'r', 'c', 'm', 'y']
labels = ['Power', 'Fertilizer', 'City Gas', 'Industrial', 'Petchem/Refineries', 'Sponge Iron/Steel']
explode = (0.2, 0, 0, 0, 0, 0)
plt.pie(values, colors=colors, labels= values,explode=explode,counterclock=False, shadow=True)
plt.title('Population Density Index')
plt.legend(labels,loc=3)
plt.show()

#Pie chart in Python with percentage values:
import matplotlib.pyplot as plt
values = [86.17, 59.86, 15.30, 20.00, 38.37, 7]
colors = ['r', 'g', 'b', 'c', 'm', 'y']
labels = ['Power', 'Fertilizer', 'City Gas', 'Industrial', 'Petchem/Refineries/Internal cons.', 'Sponge Iron/Steel']
explode = (0.2, 0, 0, 0, 0, 0)
plt.pie(values, colors=colors, labels=labels,
explode=explode, autopct='%1.1f%%',
counterclock=False, shadow=True)
plt.title('  Natural gas consumption in India (January 2013)')
#plt.legend(labels,loc=3)
plt.savefig("sample.jpg", dpi=150)
plt.show()




#Pie chart in Python with percentage values:
import matplotlib.pyplot as plt
values = [158.88, 96.85, 22.32, 27.00, 65.01, 8.00]
colors = ['b', 'g', 'r', 'c', 'm', 'y']
labels = ['Power', 'Fertilizer', 'City Gas', 'Industrial', 'Petchem/Refineries', 'Sponge Iron/Steel']
explode = (0.2, 0, 0, 0, 0, 0)
plt.pie(values, colors=colors,labels=labels, 
explode=explode, autopct='%1.1f%%',
counterclock=False, shadow=True)
plt.title('2016-17Population Density Index')
#plt.legend(labels,loc=3)
plt.show()


#Pie chart in Python with percentage values:
import matplotlib.pyplot as plt
values = [238.88, 107.85, 46.25, 37.00, 81.99, 10]
colors = ['b', 'g', 'r', 'c', 'm', 'y']
labels = ['Power', 'Fertilizer', 'City Gas', 'Industrial', 'Petchem/Refineries', 'Sponge Iron/Steel']
explode = (0.2, 0, 0, 0, 0, 0)
plt.pie(values, colors=colors, labels=labels,
explode=explode, autopct='%1.1f%%',
counterclock=False, shadow=True)
plt.title('2021-22Population Density Index')
#plt.legend(labels,loc=3)
plt.show()



#Pie chart in Python with percentage values:
import matplotlib.pyplot as plt
values = [353.88, 110.05, 85.61, 63.91, 118.85, 13.73]
colors = ['b', 'g', 'r', 'c', 'm', 'y']
labels = ['Power', 'Fertilizer', 'City Gas', 'Industrial', 'Petchem/Refineries', 'Sponge Iron/Steel']
explode = (0.2, 0, 0, 0, 0, 0)
plt.pie(values, colors=colors, labels=labels,
explode=explode, autopct='%1.1f%%',
counterclock=False, shadow=True)
plt.title('2029-30Population Density Index')
#plt.legend(labels,loc=3)
plt.show()