def ChkPrime(size):
    prime=[]
    for i in size:
        k=0
        for j in range(1,i):
            if (i%j==0):
                k=k+1
        if k==1:
            prime.append(i)
    return prime


def listPrime(addPrime):
    sum=0
    for i in range(len(addPrime)):
        sum=sum+addPrime[i]
    return sum


def main():
    print("Numbers in a list")
    no=int(input())
    size=[]
    for i in range(no):
        size.append(int(input()))
    print("The numbers entered in a list is :",size)

    no1=ChkPrime(size)
    print("The prime numbers in list is :", no1)

    no2=listPrime(no1)
    print("The addition of prime numbers in a list is :", no2)


if __name__=="__main__":
    main()