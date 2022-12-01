"""
write a short python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n
"""
def sum_odd_positive(n):
    odd_pos = []
    for i in range(n-1,0,-1):
        if not i % 2 == 0:
            odd_pos.append(i**2)
    addition = sum(odd_pos)
    return addition

n = int(input("Enter any positive integer: "))
iObj = sum_odd_positive(n)
print("Sum of the odd positive is", iObj)