x = int(input("Enter number x: "))  #added by me
y = int(input("Enter number y: "))  #added by me
try:
    ratio = x / y
    print(ratio)                    #added by me
except ZeroDivisionError:
    print("Division by zero makes it infinite, enter number other than zero")   #added by me