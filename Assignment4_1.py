def square(num):
    power=lambda num:num**2
    return power(num)

def main():
    print("Enter the number you want the square")
    no=int(input())
    sq=square(no)
    print("The square of the number is :", sq)

if __name__=="__main__":
    main()