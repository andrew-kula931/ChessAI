import matplotlib.pyplot as plt
import numpy as np

'''

This is a simple quadratic graph that auto formats the axies 
to fit the screen evenly

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create the plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Profits')
plt.title('My Organization Plan')

# Save the plot to a file
plt.savefig('Example_Plot.png')

'''

'''

This shows a very simple graph following the points given

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()

'''

'''

Random upwards plot of circles

np.random.seed(193208423)  # Random number generator
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')

plt.show()

'''

'''

Graphs a linear, quadratic, and cubic line

x = np.linspace(0, 2, 100)  # Sample data.

plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) Axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()

plt.show()

'''

'''

Creates two scribble graphs using a function

def plot_graph(ax, data1, data2, param_dict):
    out = ax.plot(data1, data2, **param_dict)
    return out


data1, data2, data3, data4 = np.random.randn(4, 100)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
plot_graph(ax1, data1, data2, {'marker': 'x'})
plot_graph(ax2, data3, data4, {'marker': 'o'})
plt.show()

'''
