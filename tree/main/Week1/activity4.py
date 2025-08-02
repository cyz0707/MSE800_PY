# week1- activity 4: Rainfall Analysis with NumPy
# Sample rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]

# Tasks: 
# Convert the list to a NumPy array and print it.
# Print the total rainfall for the week.
# Print the average rainfall for the week.
# Count how many days had no rain (0 mm).
# Print the days (by index) where the rainfall was more than 5 mm.
# Share your GitHub link on Teams when you have done.
 
import numpy as np

rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]
arr = np.array(rainfall)

print("NumPy array: ", arr)
print("total rainfall: ", np.sum(rainfall))
print("average rainfall: ", np.mean(rainfall))
print("no rain days: ", np.size(np.where(arr == 0.0)))
print("rainfall was more than 5 mm: ", np.where(arr > 5))
