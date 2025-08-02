# Develop a Python project to perform the following tasks:
# 1. Calculate and print the average temperature for the week using NumPy.
# Temperature data (in °C): [18.5, 19, 20, 25.0, 2, 30, 13.9]
# 2. Determine and display the highest and lowest recorded temperatures.
# 3. Convert all temperatures to Fahrenheit and print the converted values.
# (Use the formula: F = C × 9/5 + 32)
# 4. Identify and print the indices of days where the temperature exceeded 20°C.

import numpy as np

weekTemp = [18.5, 19, 20, 25.0, 2, 30, 13.9]
arr = np.array(weekTemp)

def overTemps():
    for i in np.where(arr > 20):
        return i

print("average temperature: ", np.mean(weekTemp))
print("highest temperature: ", np.max(weekTemp), "lowest temperature:", np.min(weekTemp))
print("Fahrenheit temperature: ", arr * 9 / 5 + 32)
print("temperature exceeded 20°C: ", overTemps())
