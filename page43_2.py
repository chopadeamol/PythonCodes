"""
Traditional method: Factors of a number 
"""
# def factors(n):
#     factor = []
#     for k in range(1, n+1):
#         if n % k == 0:
#             factor.append(k)
#     return factor

# n = int(input("Enter a number: "))
# print(list(factors(n)))

"""
List Comprehension: Factors of a numner
"""
def fact(n):
    factors = [k for k in range(1, n+1) if n % k == 0]
    return factors
print(fact(int(input("Enter number: "))))

