class Arithmetic:
    def __init__(self):
        self.value1=0
        self.value2=0

    def Accept(self):
        print("Enter value1")
        self.value1=int(input())

        print("Enter value2")
        self.value2=int(input())

    def Addition(self):
        result=self.value1+self.value2
        return result

    def Substraction(self):
        result=self.value1-self.value2
        return result

    def Multiplication(self):
        result=self.value1*self.value2
        return result

    def Division(self):
        result=self.value1/self.value2
        return result

def main():
    obj=Arithmetic()
    obj.Accept()

    retAdd=obj.Addition()
    print("The addition is :", retAdd)

    retSub=obj.Substraction()
    print("Substraction is :", retSub)

    retMult=obj.Multiplication()
    print("The multiplication is :", retMult)

    retDiv=obj.Division()
    print("The division is :", retDiv)

if __name__=="__main__":
    main()






