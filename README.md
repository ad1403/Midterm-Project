# Midterm-Project
## Package Summary
For my project, the packages I used were NumPy and Matplotlib. 
NumPy, which stands for Numerical Python, is used for working with arrays to perform mathematical and logical operations. Arrays are considered a grid of values, all of the same type. This package can also act as a random number generator. 
Matplotlib is a package that creates visualizations and allows you to plot graphs in Python. Matplotlib has the capability to create various types of graphs such as bar graphs, histograms, line graphs, scatter plots, and stem plots. 
## Install and Run Instructions
To install both of the packages, the steps are very similar. The first thing to do is to make sure that your system is updated with the most recent version of Python and that pip is downloaded and upgraded if it needs to be. From here you can install the different packages. 

To install NumPy:
```python
pip3 install numpy
```

To install Matplotlib:
```python
pip3 install matplotlib
```

## Code
My code is used to randomly generate plots and plot them afterwards. Lines 4 through 7 is the function used to generate random plots and puts it into a list. Lines 19 through 12 are responisble for getting the lists generated from the previous function in order to plot the points. Lines 14 through 16 runs the function to plot the points on a graph. 
```python
import numpy as np
import matplotlib.pyplot as plt

def get_coordinates(lst):
    for i in range(0,11):
        lst.append(np.random.randint(11))
    return lst

x = []
x_lst = get_coordinates(x)
y = []
y_lst = get_coordinates(y)

plt.plot(x_lst,y_lst,'o',color='blue',zorder=2)
plt.grid()
plt.show()
```

## Future idea
Although my current code might not transition over to real-world data, the current packages used have the ability to be useful when working with analytics and data visualization. One example, where these packages prove to be useful is when working with data like women shoe sales as NumPy can find the average amount of sales per shoe brand and from there, Matplotlib is able to plot the data on a graph to provide visuals. 
