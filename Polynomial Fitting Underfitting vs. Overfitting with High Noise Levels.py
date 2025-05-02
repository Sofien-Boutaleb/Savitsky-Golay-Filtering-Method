import numpy as np
import matplotlib.pyplot as plt
# Generate some data: True quadratic function without noise
def true_function(x):
    return 3 * x**2 + 2 * x + 1
# Generate highly noisy data with fewer points
np.random.seed(0)  # For reproducibility
x = np.linspace(0, 10, 10)  # Reduced number of points
y_true = true_function(x)
# Add much higher noise to the data to make the difference clear
y_noisy = y_true + np.random.normal(0, 50, size=x.shape)  # High noise level
# Polynomial degrees to demonstrate the effect
degrees = [2, 10]  
# Create a plot
plt.figure(figsize=(12, 6))
# Plot original true function
plt.plot(x, y_true, label='True Function: $3x^2 + 2x + 1$', color='blue', linewidth=2)
# Plot noisy data
plt.scatter(x, y_noisy, color='black', label='Highly Noisy Data', zorder=5)
# Loop through different degrees
for degree in degrees:
    # Fit polynomial to the noisy data
    coeffs = np.polyfit(x, y_noisy, degree)
    poly = np.poly1d(coeffs)
    # Generate y values for the fitted polynomial
    y_fit = poly(x)
    # Plot the fitted polynomial
    plt.plot(x, y_fit, label=f'Polynomial Degree {degree}')
# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polynomial Fitting: Underfitting vs Overfitting (High Noise)')
plt.legend()
plt.grid(True)
# Show the plot
plt.show()
