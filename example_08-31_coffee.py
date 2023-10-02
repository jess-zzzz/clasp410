# this is a comment

'''
this is a docstring. use docstrings as descriptions for functions,
primary documentation, etc.
'''

'''
Coffee problem in class (08-31)
'''

import numpy as np
import matplotlib.pyplot as plt

# create time array
t_final, t_step = 600, 1    # in seconds
t = np.arange(0, t_final, t_step)



def solve_temp(t, k=.005, T_env=25, T_init=90):
    '''
    This function takes takes an array of times and returns an array of temperatures
    corresponding to each time.

    Parameters
    ==========
    t: numpy array of time
        array of time inputs for which you want corresponding temps
    
    Other Parameters
    ================
    k: Newton cooling constant
    T_env: temperature of environment
    T_init: initial temperature of coffee

    Returns
    =======
    T: array of temperature outputs corresponding given time inputs

    '''

    T = T_env + (T_init - T_env) * np.exp(-k * t)
    
    return T

def time_to_targ(T_targ, k=0.005, T_env=20, T_init=90):
    '''
    Given an initial temperature 'T_init', an ambient temperature 'T_env',
    and a cooling rake, return the time required required to reach a target
    temperature 'T_targ'.
    '''

    t = -1/k * np.log((T_targ - T_env)/(T_init-T_env))
    return t


# solve our coffee problem
T_cream = solve_temp(t, T_init=85)
T_nocream = solve_temp(t, T_init=90)

# get time to drinkable temp
t_cream = time_to_targ(60, T_init=85)   # scenario 1: add cream in at beginning
t_nocream = time_to_targ(60, T_init=90) # scenario 2: add cream in at end (at desired temp)
t_smart = time_to_targ(65, T_init=90)   # class solution: add cream in at 65 deg.


## Plot!!

# create figure and axes objects
fig, ax = plt.subplots(1,1)

# plot lines, label
ax.plot(t, T_nocream, label="No cream til cool")
ax.plot(t, T_cream, label="Cream right away")

ax.axvline(t_nocream, color='r', ls='--', label="No cream: T=60")
ax.axvline(t_cream, color='b', ls='--', label="Cream: T=60")
ax.axvline(t_smart, color='gray', ls='--', label="No Cream: T=65")

ax.legend(loc='best')
fig.tight_layout()

plt.show()