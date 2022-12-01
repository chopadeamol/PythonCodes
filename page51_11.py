"""
Demonstrate how to use python's list comprehension syntax to produce the list [1,2,4,8,16,32,64,128,256]
"""
def multi(n):
    multiple = []
    for i in range(1,n+1):
        if n%i==0:
            multiple.append(i)
    return multiple
n = int(input("Enter a number: "))
iObj = multi(n)
print(iObj)


"""
List comprehension implementation
"""
n = int(input("Enter a number for comprehension: "))
factors = [i for i in range(1,n+1) if n%i==0]
print(factors)