"""
Give a single line commmand that computes the sum from "page51_6.py" relying on python's comprehension syntax and the built in sum function
"""

n = int(input("Enter any positive integer: "))
odd_sum = sum([i*i for i in range(n-1,0,-1) if not i%2 == 0])
print("odd positive interger sum is :",odd_sum)