import numpy as np
import matplotlib.pyplot as plt

#funciton generates random points and puts it into a list
def get_coordinates(lst):
    for i in range(0,11):
        lst.append(np.random.randint(11))
    return lst

#Getting lists in order to plot the points
x = []
x_lst = get_coordinates(x)
y = []
y_lst = get_coordinates(y)

#plotting the points
plt.plot(x_lst,y_lst,'o',color='blue',zorder=2)
plt.grid()
plt.show()
