import numpy as np
import math

Z0 = 1136
end = 30
list_of_values = [0]
lag = 3

# generate the values
for i in range(end):
    Z = 4781 * Z0 + 8521
    Z = Z % 16384
    Z1 = Z / 16384
    list_of_values.append(Z1)
    Z0 = Z

# sort the values and change the type so can calculate later
list_of_values.sort()
list_of_values = np.array(list_of_values)

# find probabilities
list_of_probabilities = np.linspace(0, 1, end+1)

#find max distnace
distance = abs(list_of_values - list_of_probabilities)
max_distance = max(distance)

result = (math.sqrt(end) + 0.12 + (0.11/math.sqrt(end))) * max_distance

# which is less than 0.29 so this is not right
print("KS test", round(result,3))

