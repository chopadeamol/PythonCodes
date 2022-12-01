def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric")
    elif x < 0:
        raise ValueError("x cannot be negative")
    else:
        print("unable to get the square root of the entered value")
def main():
    x = int(input("enter the input value: "))   # the input must be either int or float type as mentioned in the sqrt() function
    squareRoot = sqrt(x)
    print(squareRoot)
main()