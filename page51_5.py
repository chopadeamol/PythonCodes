"""
Give a single command that computes the sum of from "page51_4.py" relying on python's comprehension syntax and the built in sum function
"""
n = int(input("enter number:"))
sumSquare = sum([i*i for i in range(n-1,0,-1)])
print(sumSquare)