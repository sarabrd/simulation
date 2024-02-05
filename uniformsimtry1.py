import numpy as np
import matplotlib.pyplot as plt
import math

Z0 = 1136
end = 30
list_of_values = [0]

# generate the values
for i in range(end):
    Z=4781*Z0+8521 

    Z = Z % 16384
    list_of_values.append(Z)

    Z0 = Z

list_of_values.sort()
list_of_values = np.array(list_of_values)

list_of_values = list_of_values / 16384
list_of_probabilities = np.linspace(0, 1, 31)

#find max distnace
distance = abs(list_of_values - list_of_probabilities)
max_distance = max(distance)

#just plotting for KS test
#plt.plot(list_of_values, list_of_probabilities)
#plt.plot(np.linspace(0, 16384, 31), np.linspace(0, 1, 31))
#plt.savefig('plot.png')  # Save the plot to a file

result = (math.sqrt(30) + 0.12 + (0.11/math.sqrt(30))) * max_distance
# which is less than 0.29 so this is not right
print(result)


