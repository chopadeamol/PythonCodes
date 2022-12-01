def frequency(freq):
    no1=int(input())
    count=0
    for i in range(len(freq)):
        if (freq[i]==no1):
            count=count+1
    return count


def main():
    print("Enter the count you want in a list")
    no=int(input())
    size=[]
    for i in range(no):
        size.append(int(input()))
    print("The entered number in the list is :", size)

    fre=frequency(size)
    print("The match from the list is :", fre)

if __name__=="__main__":
    main()