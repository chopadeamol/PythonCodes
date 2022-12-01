class BankAccount:
    ROI=10.5
    def __init__(self,Name,Amount):
        self.Name=Name
        self.Amount=Amount

    def Display(self):
        print(f"The name of account holder is :{self.Name}")
        print(f"The balance in Bank Account is : {self.Amount}")

    def Deposit(self,depo):
        self.Amount=self.Amount+depo
        print(f"The balance amount in your account after deposit of {depo} is :{self.Amount}")

    def WithDraw(self,bal):
        self.Amount = self.Amount-bal
        print(f"The balance amount in your account after withdrawal of {bal} is :{self.Amount}")

    def CalculateInterest(self):
        calInterest=self.Amount*(BankAccount.ROI/100)
        print(f"The interest amount is : {calInterest}")

def main():
    print("Please enter name and amount subsequently")
    obj=BankAccount(Name=input(),Amount=float(input()))
    print("Please enter the amount you want to deposit")
    obj.Deposit(float(input()))
    print("Enter the amount you want to withdraw")
    obj.WithDraw(float(input()))
    obj.CalculateInterest()
    obj.Display()


if __name__=="__main__":
    main()
