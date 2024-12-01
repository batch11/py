import matplotlib.pyplot as plt
import numpy as np

# Generate values for x from -10 to 10
x = np.linspace(-10, 10, 400)

# Calculate y values for the function y = x^2
y = x**2

# Plotting the graph
plt.plot(x, y, label="y = x^2", color='violet')

# Adding title and labels
plt.title("Graph of y = x^2")
plt.xlabel("x")
plt.ylabel("y")

# Adding grid for better visibility
plt.grid(True)

# Displaying the graph
plt.show()
