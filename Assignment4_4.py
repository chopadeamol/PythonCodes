from functools import reduce

def even(no):
    return no%2==0

def square(no):
    return no**2

def addition(m,n):
    return m+n

def main():
    print("enter the count of entity in list")
    no=int(input())
    size=[]
    for i in range(no):
        size.append(int(input()))
    print("The list is :",size)

    filter1=list(filter(even,size))
    print("The even numbers after filter from list is :", filter1)

    map1=list(map(square,filter1))
    print("The square of the numbers after map is :", map1)

    reduce1=reduce(addition, map1)
    print("Addition of the numbers after reduce is :", reduce1)


if __name__=="__main__":
    main()
