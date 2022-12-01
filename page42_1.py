def foo(n):
    if n >= 0:
        param = n
    else:
        param = -n

    return param

def main():
    param = int(input("enter number: "))
    result = foo(param)                     # call the function
    print(result)

main()
