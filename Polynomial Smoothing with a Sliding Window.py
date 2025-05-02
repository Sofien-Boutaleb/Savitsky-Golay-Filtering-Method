import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

# Given data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 6, 5])

# Define window size
window_size = 3

# Colors for different polynomial fits
colors = ['blue', 'green', 'orange']

# Generate the figure
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='red', label='Original Data', zorder=3)

# Fit and plot polynomials for each window
for i in range(len(x) - window_size + 1):
    x_window = x[i:i + window_size]
    y_window = y[i:i + window_size]
    
    # Fit a quadratic polynomial
    coeffs = np.polyfit(x_window, y_window, 2)
    poly_eq = np.poly1d(coeffs)
    
    # Generate smooth x values for plotting
    x_smooth = np.linspace(x_window[0], x_window[-1], 100)
    y_smooth = poly_eq(x_smooth)
    
    # Plot the polynomial fit
    plt.plot(x_smooth, y_smooth, color=colors[i], linestyle='dashed', label=f'Fit {i+1}')

# Overall smoothed curve using piecewise quadratic fits
x_smooth_all = np.linspace(min(x), max(x), 100)
y_smooth_all = np.interp(x_smooth_all, x, y)
plt.plot(x_smooth_all, y_smooth_all, color='black', label='Smoothed Curve', linewidth=2)

# Labels and legend
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Moving Window Least-Squares Polynomial Approximation')
plt.legend()
plt.grid()
plt.show()
