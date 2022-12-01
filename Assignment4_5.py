from functools import reduce

def prime(no):
    for i in range(2,no):
        if (no%i==0):
            return
    else:
        return no

def multiplyBy2(num):
    return num*2

def maximum(num1,num2):
    return max(num1,num2)

def main():
    print("enter the count of entity in a list")
    no=int(input())
    size=[]
    for i in range(no):
        size.append(int(input()))
    print("The list is :", size)

    filter1=list(filter(prime,size))
    print("The prime numbers from a list is :", filter1)

    map1=list(map(multiplyBy2,filter1))
    print("The multiplication of numbers after map is :", map1)

    reduce1=reduce(maximum,map1)
    print("The maximum number after reduce is :", reduce1)


if __name__=="__main__":
    main()