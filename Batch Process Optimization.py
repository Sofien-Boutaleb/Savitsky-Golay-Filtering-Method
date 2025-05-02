import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Given data
time = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
concentration = np.array([1.0, 0.85, 0.75, 0.65, 0.60, 0.55, 0.50, 0.45, 0.42, 0.38, 0.35])

# Apply Savitzky-Golay filter
smoothed_concentration = savgol_filter(concentration, window_length=5, polyorder=2)

# Compute the numerical derivative before and after filtering
original_derivative = np.gradient(concentration, time)
smoothed_derivative = np.gradient(smoothed_concentration, time)

# Plot original and smoothed data
plt.figure(figsize=(10, 5))

# Plot concentration curves
plt.subplot(1, 2, 1)
plt.plot(time, concentration, 'o-', label='Original Data', markersize=5)
plt.plot(time, smoothed_concentration, 's-', label='Smoothed Data (Savitzky-Golay)', markersize=5)
plt.xlabel('Time (hours)')
plt.ylabel('Concentration of A')
plt.title('Original vs. Smoothed Concentration')
plt.legend()
plt.grid(True)

# Plot derivative curves
plt.subplot(1, 2, 2)
plt.plot(time, original_derivative, 'o-', label='Original Derivative', markersize=5)
plt.plot(time, smoothed_derivative, 's-', label='Smoothed Derivative (Savitzky-Golay)', markersize=5)
plt.xlabel('Time (hours)')
plt.ylabel('d(Concentration)/dt')
plt.title('Derivative Before and After Filtering')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
