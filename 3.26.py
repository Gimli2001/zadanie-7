import matplotlib.pyplot as plt
import numpy as np

# Create x values in degrees from 0 to 360
x = np.arange(0, 361, 1)  # Step of 1 degree

# Create y values as the sine of x, converting degrees to radians
y = np.sin(np.radians(x))

# Plot the graph
plt.plot(x, y, label='y = sin(x)')

# Add labels and title
plt.xlabel('Angle (degrees)')
plt.ylabel('sin(x)')
plt.title('Graph of y = sin(x)')

# Add a legend
plt.legend()

# Display the graph
plt.grid(True)
plt.show()
