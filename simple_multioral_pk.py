#!/usr/bin/env python
# coding: utf-8

# In[106]:


# ---------------------------------------------------------------------------------------------------------------
#
#                   Simple_multioral_pk: Display Cp following multiple oral doses
#
#                               A. Rusinko  (5/23/2021) v1.00
# ---------------------------------------------------------------------------------------------------------------
import sys
import matplotlib.pyplot as plt
from math import exp


# In[159]:


# Calculate vector of time points (x-axis)
# Replace with equivalent from numpy
def timevector_create(starttime, endtime, increment):
    numpoints = int((endtime - starttime)/increment)
    #print(numpoints)
    timevalue = starttime
    timevec = [starttime]
    for i in range(1,numpoints):
        timevalue += increment
        timevec.append(timevalue)
    return timevec
       
# Calculate fraction of dose remaining
def calculate_fraction(ka, kel, xfactor, xtime):
    fraction = xfactor * (exp(-1*kel*xtime) - exp(-1*ka*xtime))
    return fraction
    


# In[164]:


# Calculate Cp given oral dose
ka  = 0.95
kel = 0.50                            # units (1/hr)

# Ratio used to relate ka and kel
xfactor = ka / (ka - kel)

# Should be estimated from Dose/Vd    
conc_plasma_initial = 500             # units (mcg / ml)

# Dosing information
number_doses    = 6
dosing_interval = 10.0                 # units (hr)

# Get vector of time data points
timevector       = timevector_create(0.0, dosing_interval, 0.05)

# Get extra long vector of time data points for example
long_timevector = timevector_create(0.0, 12.0, 0.05)
                
# Initial Dose
conc_plasma  = [conc_plasma_initial * calculate_fraction(ka,kel,xfactor,t) for t in timevector]
#print(len(conc_plasma))

conc_plasma_first = [conc_plasma_initial * calculate_fraction(ka,kel,xfactor,t) for t in long_timevector]

# Calculate NEW baseline concentration at dosing interval
conc_plasma_baseline = conc_plasma_initial * calculate_fraction(ka,kel,xfactor,dosing_interval)
#print(conc_plasma_baseline)


# In[165]:


# Display results
fig, ax = plt.subplots()

# Plot Cp for initial oral dose
#plt.plot(timevector, conc_plasma , color='red', label='Cp Oral Dose')
plt.plot(long_timevector, conc_plasma_first, color='red', linestyle='dashed',linewidth=0.75,alpha=0.75)

for i in range(1,number_doses):
    new_conc_plasma = [conc_plasma_baseline+(conc_plasma_initial * calculate_fraction(ka,kel,xfactor,t)) for t in timevector]
    print(len(new_conc_plasma), len(conc_plasma))
    conc_plasma_baseline = new_conc_plasma[-1]
    conc_plasma.extend(new_conc_plasma)

    
total_timevector = timevector_create(0, number_doses*dosing_interval, 0.05)
#print(total_timevector)
#print(conc_plasma)
  
plt.plot(total_timevector, conc_plasma , color='red', label='Cp Oral Dose')


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
plt.legend()

plt.show()


# In[ ]:





# In[ ]:




