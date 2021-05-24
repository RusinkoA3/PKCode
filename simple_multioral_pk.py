#!/usr/bin/env python
# coding: utf-8

# ---------------------------------------------------------------------------------------------------------------
#
#                     Simple_multioral_pk: Display Cp following multiple oral doses
#                   Simulation assumes one compartment model with first order kinetics.
#
#                               A. Rusinko  (5/24/2021) v1.1
# ---------------------------------------------------------------------------------------------------------------
import sys
import matplotlib.pyplot as plt
from math import exp

# Calculate vector of time points (x-axis)
# Replace with equivalent from numpy
def timevector_create(starttime, endtime, increment):
    numpoints = int((endtime - starttime)/increment) +1
    #print(numpoints)
    timevalue = starttime
    timevec = [starttime]
    for i in range(1,numpoints):
        timevalue += increment+0.00001
        timevec.append(timevalue)
    return timevec
       
# Calculate fraction of dose remaining
def calculate_fraction(ka, kel, xfactor, xtime):
    fraction = xfactor * (exp(-1*kel*xtime) - exp(-1*ka*xtime))
    return fraction


# Calculate Cp given oral dose 
ka  = 0.75
kel = 0.10                            # units (1/hr)

# Ratio used to relate ka and kel
xfactor = ka / (ka - kel)

# Should be estimated from Dose/Vd    
conc_plasma_initial = 500             # units (mcg / ml)

# Dosing information
number_doses    = 6
dosing_interval = 8.0                 # units (hr)
total_time      = number_doses * dosing_interval

# Get vector of time data points
timevector       = timevector_create(0.0, dosing_interval, 0.05)

# Get extra long vector of time data points for example and calculate Cp for first dose
long_timevector   = timevector_create(0.0, 5.0*dosing_interval, 0.05)
conc_plasma_first = [conc_plasma_initial * calculate_fraction(ka,kel,xfactor,t) for t in long_timevector]
                
# Calculate Cp for length of simulation (total_time)
total_timevector = timevector_create(0.0, total_time, 0.05) 
#print(total_timevector[0:10], "\n")

# Use independent dose assumption and superposition principle
conc_plasma = []
for xtime in total_timevector:
    n_doses    = int(xtime / dosing_interval) +1
    timeindose = xtime % dosing_interval
    #print(n_doses, xtime)

    # Total at each time point
    Cp_total = 0.0
    
    # Loop over all doses
    for i in range(0, n_doses):
        ttime = xtime- i*dosing_interval
        Cp = conc_plasma_initial * calculate_fraction(ka, kel, xfactor, ttime)
        #print(i,xtime,ttime,Cp)
        Cp_total += Cp
        
    #print(Cp_total, "\n")
    conc_plasma.append(Cp_total)


# Display results
fig, ax = plt.subplots()

# Plot Cp for initial oral dose
plt.plot(total_timevector, conc_plasma , color='red', label='Cp Oral Dose')
plt.plot(long_timevector, conc_plasma_first, color='red', linestyle='dashed',linewidth=0.75,alpha=0.75)

#
#    Make the plot pretty
#
    
# set the x-spine
ax.spines['left'].set_position('zero')

# turn off the right spine/ticks
ax.spines['right'].set_color('none')
ax.yaxis.tick_left()

# set the y-spine
ax.spines['bottom'].set_position('zero')

# turn off the top spine/ticks
ax.spines['top'].set_color('none')
ax.xaxis.tick_bottom()

# Decorate plot
plt.title("Concentration in Plasma Following Oral Dose")
plt.xlabel("Time (hours)")
plt.ylabel("Cp (mcg/ml)")
#plt.legend()

plt.show()





