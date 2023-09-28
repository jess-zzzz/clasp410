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

    T = T_env + (T_init - T_env) * np.exp(-k * time)
    
    return T

T = solve_temp(time)
print(T)
plt.plot(time, T)
plt.show()

# solve our coffee problem
t_cream = solve_temp(time, T_init=85)
t_nocream = solve_temp(time, T_init=90)

# get time to drinkable temp
t_cream = time_to_temp(60, T_init=85)
t_nocream = time_to_temp(90, T_init=90)
t_smart = time_to_temp(65, T_init=90) # add cream in at 65 deg.