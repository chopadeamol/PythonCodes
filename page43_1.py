"""
Traditional way to get the squares of a number
"""

# n = int(input("Enter a number: "))
# squares = []
# for k in range(1, n+1):
#     squares.append(k * k)
# print(squares)


"""
List comprehension to get the square of the number
"""

m = int(input("Enter a number: "))
def squares(m):
    square = [k*k for k in range(1, m+1)]
    return square
print(squares(m))
