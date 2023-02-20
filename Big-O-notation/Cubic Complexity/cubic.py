"""
A function is said to cubic if the number of steps used are a cubic function of the number of items in the
inputs
"""


def cubic_algo(array):
    for item in array:
        for item2 in array:
            for item3 in array:
                print(item, ' ', item2, ' ', item3)


array = []
size = int(input("Enter number of elements in your array: "))

print("Enter list elements: \n")

for i in range(0, size):
    element = int(input())
    array.append(element)

print(cubic_algo([4, 5, 6, 7, 8]))
