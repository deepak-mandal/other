#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 05:41:12 2021

@author: deepak
"""
#Stacked Bar Chart in Python with legends:
import matplotlib.pyplot as plt
import numpy as np
 
city=['2012-13','2016-17','2021-22','2026-27','2029-30']
Gender=['Male','Female', 'other']
#pos = np.arange(len(city))
Happiness_Index_Male=[101,156.7,182,211,230]
Happiness_Index_Female=[44.6,143.0,214,55,214]
Happiness_Index_other=[0,0,30,30,30]
 
plt.bar(city,Happiness_Index_Male,color='blue',edgecolor='black')
plt.bar(city,Happiness_Index_Female,color='pink',edgecolor='black',bottom=Happiness_Index_Male)
plt.bar(city,Happiness_Index_other,color='green',edgecolor='black',bottom=Happiness_Index_Male+Happiness_Index_Female)

#bar() function plots the Happiness_Index_Female on top of Happiness_Index_Male with the help of 
#argument  bottom=Happiness_Index_Male.
#plt.xticks(pos, city)
plt.xlabel('City', fontsize=16)
plt.ylabel('Happiness_Index', fontsize=16)
plt.title('Stacked Barchart - Happiness index across cities',fontsize=18)
plt.legend(Gender,loc=2)
plt.show()



# importing package
import matplotlib.pyplot as plt
import numpy as np
  
# create data
x = ['2012-13','2016-17','2021-22','2026-27','2029-30']
y1 = np.array([101,156.7,182,211,230])
y2 = np.array([44.6,143.0, 188.0,214,214])
y3 = np.array([0,0,30,30,30])
#y4 = np.array([10, 29, 13, 19])
  
# plot bars in stack manner
plt.bar(x, y1, color='r')
plt.bar(x, y2, bottom=y1, color='b')
plt.bar(x, y3, bottom=y1+y2, color='g')
#plt.bar(x, y4, bottom=y1+y2+y3, color='g')
#plt.xlabel("Teams")
plt.ylabel("MMSCMD")
plt.legend(['Domestic Sources','Imported LNG', 'Transnational Pipelines'])
plt.title("Natural Gas Supply Growth Profile")
plt.show()