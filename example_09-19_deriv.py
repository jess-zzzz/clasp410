#!bin asdasdf

'''
This file explores different numerical approxations for first derivatives.
'''

import numpy as np
import matplotlib.pyplot as plt

def forward_diff(f_x, dx=1):
    '''
    Take the forward difference first derivative of 'f_x'.

    '''
    # initialize array
    dfdx = np.zeros(f_x.size)
    dfdx[:-1] = (f_x[1:] - f_x[:-1]) / dx # using indexing to initialize array instead of loop!!! neat trick

    # boundary condition
    dfdx[-1] = dfdx[-2]

# Make a demo plot:
dx = 0.5
x = np.arange(0, 4*np.pi, dx)
f_x = np.sin(x)
dfdx_sol = np.cos(x)
dfdx = forward_diff(f_x, dx=dx)

plt.plot(x, dfdx_sol)
plt.plot(x, dfdx)
plt.legend()


## find error
dx_all = linspace(0.001, 1, 100)
err = []
for dx in dx_all:
    x = np.arange(0, 4*np.pi, dx)
    f_x = np.sin(x)
    dfdx_sol = np.cos(x)
    dfdx = forward_diff(f_x, dx=dx)

    # calculate error:
    err.append(np.max(np.abs(dfdx_sol - dfdx)))

fig, ax = plt.subplots(1,1)
plt.plot(dx_all, err)