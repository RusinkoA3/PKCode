#!/usr/bin/env python
# coding: utf-8

# In[42]:


# ---------------------------------------------------------------------------------------------------------------
#
#                   Simple_oral_pk: Display Cp after oral dose
#
#                         A. Rusinko  (5/23/2021) v1.00
# ---------------------------------------------------------------------------------------------------------------
import sys
import matplotlib.pyplot as plt
from math import exp, log


# In[54]:


# Calculate vector of time points (x-axis)                           
def timevector_create(starttime, endtime, increment):
    numpoints = int((endtime - starttime)/increment)
    print(numpoints)
    timevalue = starttime
    timevec = [starttime]
    for i in range(1,numpoints):
        timevalue += increment
        timevec.append(timevalue)
    return timevec


timevector = timevector_create(0.0, 8.0, 0.1)
#print(timevector)


# In[55]:


# Calculate Cp given oral dose
ka  = 0.95
kel = 0.50                            # units (1/hr)

# Should be estimated from Dose/Vd    
conc_plasma_initial = 500             # units (mcg / ml)

# Calculate theoretical absorped
entering_plasma = [conc_plasma_initial * (1.0 - exp(-1*ka*t)) for t in timevector]
#print(entering_plasma)

# Calculate theoretical eliminated
leaving_plasma  = [conc_plasma_initial * exp(-1*kel*t) for t in timevector]
#print(leaving_plasma)

# Calculate Cp
xfactor = ka / (ka - kel)
conc_plasma = [conc_plasma_initial * xfactor * (exp(-1*kel*t) - exp(-1*ka*t)) for t in timevector]

# Calculate tmax and cmax
tmax = 1.0 / (ka - kel) * log(ka/kel)
cmax = conc_plasma_initial * xfactor * (exp(-1*kel*tmax) - exp(-1*ka*tmax))
print(tmax, cmax)


# In[56]:


# Display results
fig, ax = plt.subplots()

# Plot theoretical Cp for absorption
plt.plot(timevector, entering_plasma , color='black', linestyle='dashed',linewidth=0.75,alpha=0.3,label='Absorption')

# Plot theoretical Cp for elimination
plt.plot(timevector, leaving_plasma , color='blue', linestyle='dashed',linewidth=0.75,alpha=0.3,label='Elimination')

# Plot theoretical Cp for oral dose
#plt.plot(timevector, conc_plasma , color='red', label='Cp Oral Dose')

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






