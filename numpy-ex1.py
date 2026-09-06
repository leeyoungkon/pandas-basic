import numpy as np

data = np.array([10, 20, 30, 40, 50])

print(data)
print(data[1:4])  # Slicing from index 1 to 3 (4 is exclusive)

print(data[:3])  # Slicing from the beginning to index 2 (3 is exclusive)
print(data[::2])  # Slicing with a step of 2 (every second element)
print(data[::-1])  # Slicing with a step of -1 (reversing the array)
print(data[1::2])  # Slicing from index 1 to the end with a step of 2 (every second element starting from index 1)