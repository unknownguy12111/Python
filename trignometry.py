import matplotlib.pyplot as mat
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(x / 10)
y4 = np.log(x + 1)

# Create a figure and multiple subplots
fig, ((ax1, ax2), (ax3, ax4)) = mat.subplots(2, 2, figsize=(10, 8))

# Plot 1: Sine function
ax1.plot(x, y1, color='blue')
ax1.set_title('Sine Function')

# Plot 2: Cosine function
ax2.plot(x, y2, color='red')
ax2.set_title('Cosine Function')

# Plot 3: Exponential function
ax3.plot(x, y3, color='green')
ax3.set_title('Exponential Function')

# Plot 4: Logarithmic function
ax4.plot(x, y4, color='purple')
ax4.set_title('Logarithmic Function')

# Add a title to the entire figure
fig.suptitle('Complex Visualization with Matplotlib')

# Adjust layout to prevent overlapping titles
mat.tight_layout()

# Show the plot
mat.show()