"""
An algorithm is said to be quadratic if the number of steps used are a quadratic function of
the number of items in the inputs.
"""


def quadratic_algo(items):
    for item in items:
        for item2 in items:
            print(item, ' ', item2)

array = []
size = int(input("Enter number of elements in your array: "))

print("Enter list elements: \n")

for i in range(0, size):
    element = int(input())
    array.append(element)

print(quadratic_algo(array))
