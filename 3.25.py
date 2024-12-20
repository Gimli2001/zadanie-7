import matplotlib.pyplot as plt

# Initialize lists for x and y values
x = []
y = []

# Create x values
for n in range(-100, 101):
    x.append(n)

# Create y values
for n in x:
    y.append(n**2 - 3)

# Plot the graph
plt.plot(x, y, label='f(x) = x^2 - 3')

# Add labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x) = x^2 - 3')

# Add a legend
plt.legend()

# Display the graph
plt.grid(True)
plt.show()
