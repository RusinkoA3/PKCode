#!/usr/bin/env python
# coding: utf-8

# In[77]:


# ---------------------------------------------------------------------------------------------------------------
#
#                   Simple_iv_pk: Display a first order elimination after iv bolus dose
#
#                                       A. Rusinko  (5/23/2021) v1.00
# ---------------------------------------------------------------------------------------------------------------
import sys
import matplotlib.pyplot as plt
from math import exp


# In[106]:


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

timevector = timevector_create(0.0, 8.0, 0.05)
#print(timevector)


# In[107]:


# Calculate Cp given iv bolus
kel = 0.50                            # units (1/hr)

conc_plasma_initial = 500             # units (mcg / ml)

conc_plasma = [conc_plasma_initial * exp(-1*kel*t) for t in timevector]
#print(conc_plasma)


# In[108]:


# Display results
fig, ax = plt.subplots()
plt.plot(timevector, conc_plasma , color='blue', linestyle='dashed',linewidth=0.5,label='Elimination')

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




