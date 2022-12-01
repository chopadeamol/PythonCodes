def mini(lis):
    minimum=min(lis)
    return minimum


def main():
    print("Please enter the numbers you want in a list")
    no=int(input())
    size=[]
    for i in range(no):
        size.append(int(input()))
    print("The input list is :", size)
    mi=mini(size)
    print("The minimum number from the list is :", mi)


if __name__=="__main__":
    main()
