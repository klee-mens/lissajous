# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 17:15:13 2020

@author: mens
"""

import numpy as np
import matplotlib.pyplot as plt

a = 0.3
phi = 2.0*np.pi * 0.9

b = np.sqrt(1-a**2)
t = np.linspace(0, 2*np.pi, 1000)

x = np.real(a*np.exp(1.0j*t))
y = np.real(b*np.exp(1.0j*(t + phi)))

plt.plot(x, y)
