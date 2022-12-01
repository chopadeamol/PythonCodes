class Circle:
    PI=3.14
    def __init__(self):
        self.Radius=0.0
        # self.Area=0.0
        # self.Circumference=0.0


    def Accept(self):
        print("Enter the value of radius")
        self.Radius = float(input())

    def CalculateArea(self):
        self.Area =self.PI * self.Radius * self.Radius
        return self.Area

    def CalculateCircumference(self):
        self.Circumference=2 * self.PI * self.Radius
        #print("The circum :",self.Circumference)
        return self.Circumference

    def Display(self):
        print("The area of a circle is :",self.CalculateArea())
        print("The circumference of circle is :", self.CalculateCircumference())

def main():
    obj=Circle()
    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()

if __name__=="__main__":
    main()