"""
Write a short python function, is_multiple(n,m), that takes two integer values and returns True if n is a multiple of m, that is n= mi for some integer i, and False otherwise
"""
import sys
def is_multiple(n,m):
    for i in range(n+1):
        if n == m * i:
            return True
    else:
        return False

print("Enter any two integer number: ")
# k = int(input("Enter first integer: "))
# j = int(input("Enter second integer: "))
g, h = len(sys.argv)
multiple = is_multiple(g, h)
print(multiple)