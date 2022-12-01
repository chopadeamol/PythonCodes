def mult(x,y):
    multi=lambda x,y:x*y
    return multi(x,y)

def main():
    print("Put the number")
    no1,no2=map(int,input().split())
    no3 = mult(no1,no2)
    print("The multiplication of number is :", no3)


if __name__=="__main__":
    main()