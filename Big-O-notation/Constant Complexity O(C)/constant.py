#Constant time 

"""
The complexity of an algorithm is said to be constant if the time required to complete the execution
of the algorithm is constant, irrespective of the number of inputs.
"""


def array_mult(items):
    prod = items[0] * items[0]
    return prod

array = []
size = int(input("Enter number of elements in your array: "))

print("Enter list elements: \n")

for i in range(0, size):
    element = int(input())
    array.append(element)


print(array_mult(array))
