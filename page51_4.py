"""
Write a short python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n
"""
def sum_square(square):
    power = []
    for i in range(square-1,0,-1):
        power.append(i**2)
    add = sum(power)
    return add

iInput = int(input("Enter any positive integer: "))
iObj = sum_square(iInput)
print("Sum of square of positive integer than the given input is: ", iObj)