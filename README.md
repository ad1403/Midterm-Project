# Midterm-Project
# Package Summary
The packages used within the presented code sequence is NumPy and Matplotlib. 
NumPy, which stands for Numerical Python is used for working with arrays to perform mathematical and logical operations. 
Matplotlib is a package that creates visualizations like graphs in Python. 
Install and Run Instructions. How to install the packages necessary to run your code
Code. Brief explanation of how your code works and highlights of important areas with line numbers included.

```python
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
```


Future idea. What if I asked you to use this package in your final class project? Describing one idea, including explaining what this package would do in that project.
