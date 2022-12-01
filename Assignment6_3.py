class Arithmetic:
    def __init__(self,value):
        self.value=value

    def ChkPrime(self):
        for i in range(2,self.value):
            if self.value%i==0:
                return False
        else:
            return True

    def ChkPerfect(self):
        sum=0
        for i in range(1, self.value):
            if self.value%i==0:
                sum=sum+i
        return sum==self.value

    def SumFactors(self):
        count=0
        for i in range(1,self.value):
            if self.value%i==0:
                count=count+i
        return count

    def Factors(self):
        for i in range(1, self.value+1):
            if self.value%i==0:
                print(i)
            break


def main():
    print("Enter the value")
    obj=Arithmetic(value=int(input()))

    obj.ChkPrime()
    print("Is number prime? :",obj.ChkPrime())

    obj.ChkPerfect()
    print("Is it a perfect number? :", obj.ChkPerfect())

    obj.SumFactors()
    print("The addition of factors are :",obj.SumFactors())

    obj.Factors()
    print("The factors of a number is :",obj.Factors())

if __name__=="__main__":
    main()