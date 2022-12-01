class Demo:
    Value=0
    def __init__(self,a,b):
        print("Inside constructor")
        self.no1=a
        self.no2=b

    def fun(self):
        print("The value of number1 and number2 in fun is :", self.no1, self.no2)


    def gun(self):
        print("The values of number1 and number2 in gun is :",self.no1, self.no2)

def main():
    print("Enter the first number")
    x=int(input())

    print("Enter the second number")
    y=int(input())

    obj=Demo(x,y)


    obj1=Demo(11, 21)
    obj2=Demo(51, 101)

    obj1.fun()
    obj2.fun()
    obj2.gun()
    obj2.gun()


if __name__=="__main__":
    main()

