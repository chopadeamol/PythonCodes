from functools import reduce

def Filt(num):
    if num>=70 and num<=90:
        return num

def Map(num):
    return num+10

def Reduced(a,b):
    return a*b


def main():
    no=int(input("Enter a number you want to put in list"))
    listed=[]
    for i in range(no):
        listed.append(int(input("Enter numbers ")))
    print("Listed numbers are :", listed)

    strained=list(filter(Filt,listed))
    print("Data after filter is :", strained)

    Increased=list(map(Map, strained))
    print("Data after map is :", Increased)

    Integrate=reduce(Reduced, Increased)
    print("Data after reduce is :", Integrate)


if __name__=="__main__":
    main()