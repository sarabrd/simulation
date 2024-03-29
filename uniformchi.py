import numpy as np
import math

Z0 = 1136
end = 50
list_of_values = []

# generate the values
for i in range(end):
    Z = 4781 * Z0 + 8521
    Z = Z % 16384
    Z1 = Z / 16384
    list_of_values.append(Z1)
    Z0 = Z

# reshape the list into 2d vectors
random_vectors = np.array(list_of_values).reshape(-1, 2)

##find the frequency values to later use to find differences
frequencies = np.zeros((3, 3))

# count the number of instances in each square
for vector in random_vectors:
    x_index = min(int(vector[0] * 3), 2)
    y_index = min(int(vector[1] * 3), 2)
    frequencies[x_index, y_index] += 1

#calculations and printing the result
expected = 25/9
difference_squared_divided = ((frequencies - expected)**2)/expected
chi = np.sum(difference_squared_divided)
print("chi_squared:", chi)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##Autocorrelation
lag = 3
h = math.floor((end-1)/lag) - 1
every_third = list_of_values[::lag]

# Initialize the sum
sum_of_products = 0

# Iterate over the vector and calculate the sum of products
for i in range(len(every_third) - 1):
    sum_of_products += every_third[i] * every_third[i + 1]

corr = 12 / (h + 1) * sum_of_products - 3
Aj = corr / (math.sqrt(((13 * h + 7) /(h + 1)**2)))
print("Aj:", Aj)

