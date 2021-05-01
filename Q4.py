#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Roll no: 170122014
Question 4:    
"""
import math

rw= (5+0.5)/12	#gas_well_diameter/2
specific_gravity= 0.7

drainage_area= 100
re= (4356000/(22/7))**0.5   #for 100 acre; effective_drainage_radius
p_bar= 5000	#average reservoir pressure in psia
pwf= 3000	#bottom hole pressure in psia
T= 150	#average_reservoir_temperature, in degree F

k= 0.20  #effective permeabilty, in md
h= 60	#thickness of pay zone in ft

av_z = 0.0121   #average value of z
av_mu = 0.935   #average value of mu 

skin_factor=4
D= 0.002 	#non- Darcy coefficient in day/MScf

Bg= 0.00504*av_z*(T+460)/p_bar

"""
using Pressure approximation approach
"""
#q1 or q2 or q3 and so on are the gas production rate in Mscf/d,
upper_term=k*h*(p_bar-pwf)
lower_term= 141.2*10**3*Bg*av_mu*(math.log((0.472*re*2/rw)))

q1= (upper_term)/(lower_term)

print("4.1 The value of flow rate using p- approximation (q1) = {:.2f} Mscf/day".format(q1))

"""
using pressure square approach, flow rate, q2
"""
q2=(k*h*(p_bar**2-pwf**2))/(1424*(T+460)*av_mu*av_z*(math.log(0.472*re*2/rw)))
print("4.2.The value of flow rate using p-square approximation (q2) = {:.2f} Mscf/day".format(q2))
print()
"""
% reduction
"""
q3= (k*h*(p_bar-pwf))/(141.2*10**3*Bg*av_mu*(math.log((0.472*re*2/rw)))+skin_factor)
print("q3= {} Mscf/day".format(q3))

percentage_reduction= ((q1-q3)/q1)*100
print("4.3. Reduction (%) in the of flow rate (p- approximation) = {:.2f} %".format(percentage_reduction))

productivity_index=q3/(p_bar-pwf)
print("4.4. The value of the Productivity index (J) for Q-4.3 is = {:.2f}".format(productivity_index))

"""
4.5. The value of flow rate (pressure square approximation, Mscf/day) if the values of
non- Darcy coefficient D = 0.002 day/MScf and skin factor = 4,
"""
def func(x): 
	return 0.002*x**2+(skin_factor+math.log((0.472*re*2/rw)))*x-(k*h*(p_bar**2-pwf**2))/(1424*(T+460)*av_mu*av_z)

# Derivative of this function  
def derivFunc(x): 
	return 2*0.002*x+(skin_factor+math.log((0.472*re*2/rw)))

# Function to find the root 
def newtonRaphson(x):
	h = func(x) / derivFunc(x) 
	while abs(h) >= 0.0001: 
		h = func(x)/derivFunc(x)
		# x(i+1) = x(i) - f(x) / f'(x) 
		x=x-h
	return x
        
x0 = 0 # Initial Guess (can be derive from rough graph)
q4=newtonRaphson(x0)
print("4.5. The value of flow rate (pressure square approximation) is = {:.2f} Mscf/day".format(q4))

"""
Q 4.6
"""

def func2(x):
	pwf=0
	return 0.002*x**2+(skin_factor+math.log((0.472*re*2/rw)))*x-(k*h*(p_bar**2-pwf**2))/(1424*(T+460)*av_mu*av_z)

# Derivative of this function  
def derivFunc2(x): 
	return 2*0.002*x+(skin_factor+math.log((0.472*re*2/rw)))

# Function to find the root 
def newtonRaphson2(x):
	h = func2(x) / derivFunc2(x) 
	while abs(h) >= 0.0001: 
		h = func2(x)/derivFunc2(x)
		# x(i+1) = x(i) - f(x) / f'(x) 
		x=x-h
	return x
 
x0 = 0 # Initial Guess (can be derive from rough graph)
q5=newtonRaphson2(x0)
print("4.6. The value of flow rate for Q-4.5 (when bottom hole pressure is at maximum rate) = {:.2f} Mscf/day".format(q5))
print()
"""
the testing data are available for the same well at two stabilized 
flow rates, 1200 Mscf/d (BHP: 4200 psia) and 3600 Mcsf/d (BHP: 1250 psia).
"""
pwf1=4200
pwf2=1250
q1=1200
q2=3600

B=((p_bar**2-pwf1**2)*q2 - (p_bar**2-pwf2**2)*q1 )/(q1**2*q2-q2**2*q1)

A=((p_bar**2-pwf1**2)-B*q1**2)/q1

print("A=", A)
print("B=", B)
print("4.7. The IPR from Forchheimer model considering pressure square approximation is given by: ")
print("Pr^2 - Pwf^2 = {:.2f}q + {:.2f}q^2".format(A, B))
print()

"""

"""
n= (math.log(q1/q2))/(math.log((p_bar**2-pwf1**2)/(p_bar**2-pwf2**2)))

C= q1/(p_bar**2-pwf1**2)**n

print("n= ", n,", and C= ", C)
print("4. 8. The IPR from Back pressure model considering pressure square approximation is given by: ")
print("q = {:.6f}[Pr^2 - Pwf^2]^{:.2f}".format(C, n))
print()
"""
Forchheimer model considering pressure square approximation
"""
def func3(x): 
	return 5944.792*x+0.157118*x**2-5000**2

# Derivative of this function  
def derivFunc3(x): 
	return 5944.792+0.157118*x*2 

# Function to find the root 
def newtonRaphson3(x):
	h = func3(x) / derivFunc3(x) 
	while abs(h) >= 0.0001: 
		h = func3(x)/derivFunc3(x)
		# x(i+1) = x(i) - f(x) / f'(x) 
		x=x-h 
	return x
	
x0 = 0 # Initial Guess (can be derive from rough graph)
q7= newtonRaphson3(x0)

print("4.9 The absolute open flow (AOF) value from Forchheimer model considering pressure square approximation is = {:.2f}".format(q7))
