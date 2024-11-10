import numpy as np

# Parameters
sampling_frequency = 800000  # Sampling frequency in Hz
signal_frequency = 40000  # Signal frequency in Hz
time_period = 1 / signal_frequency  # Period of the signal
duration = 5 * time_period  # Duration for 5 periods of the signal
time_array = np.linspace(0, duration, int(sampling_frequency * duration))

# Phase shifts from the given data
phases = [0, -125.307, 125.854, -51.923, 102.847]  # in degrees
phases_rad = [np.deg2rad(phase) for phase in phases]  # Convert to radians

# Generate the sine waves with the given phase shifts
signals = [np.sin(2 * np.pi * signal_frequency * time_array + phase) for phase in phases_rad]
print(signals[0])
print(signals[1])
print(signals[2])
print(signals[3])
print(signals[4])


# # Plot the sine waves
# plt.figure(figsize=(12, 8))
# for i, signal in enumerate(signals):
#     plt.plot(time_array, signal, label=f'Signal {i+1} (Phase: {phases[i]}°)')

# # Graph settings
# plt.title('Sine Waves with Different Phase Shifts')
# plt.xlabel('Time (seconds)')
# plt.ylabel('Amplitude')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()

# # Display the graph
# plt.show()
