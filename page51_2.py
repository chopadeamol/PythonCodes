"""
R-1.2: Write a short python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo or division operators.
"""
def is_even(k):
    is_even = True
    for i in range(1,k+1):
        if is_even == True:
            is_even = False
        else:
            is_even = True
    return is_even


k = int(input("enter any integer: "))
even = is_even(k)

print("is number even ? :->", even)
