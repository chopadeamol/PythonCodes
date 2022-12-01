def foo(n):
    param = n if n >=0 else -n
    return param


n = int(input("Enter number: "))

result = foo(n)
print(result)