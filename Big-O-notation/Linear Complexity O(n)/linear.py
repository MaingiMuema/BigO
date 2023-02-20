"""
The complexity of an algorithm is said to be linear if the time required to complete the execution
increases or decreases linearly with the number of inputs.
"""


def linear_algo(items):
    for item in items:
        print(item)

array = []
size = int(input("Enter number of elements in your array: "))

print("Enter list elements: \n")

for i in range(0, size):
    element = int(input())
    array.append(element)

print(linear_algo(array))
