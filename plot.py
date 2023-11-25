#Build a plot to compare the Taylor Series approximation to Python's cos() function


import math
import numpy as np
import matplotlib.pyplot as plt

def func_cos(x, n_terms):
    result = 0
    for n in range(n_terms):
        term = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
        result += term
    return result

angles = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
p_cos = np.cos(angles)

fig, ax = plt.subplots()
ax.plot(angles, p_cos)

# add lines for between 1 and 6 terms in the Taylor Series
for i in range(1, 6):
    t_cos = [func_cos(angle, i) for angle in angles]
    ax.plot(angles, t_cos)

ax.set_ylim([-2, 2])  # Adjusted the y-axis limit for better visualization

# set up legend
legend_lst = ['cos() function']
for i in range(1, 6):
    legend_lst.append(f'Taylor Series - {i} terms')
ax.legend(legend_lst, loc=3)

plt.show()
