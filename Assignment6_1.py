class BookStore:
    NoOfBooks=0
    def __init__(self,Name,Author):
        self.Name=Name
        self.Author=Author
        BookStore.NoOfBooks +=1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of Books : {BookStore.NoOfBooks}")
        # print("The Author of Book is :", self.Author)
        # print("The number of Books are :", BookStore.NoOfBooks)

def main():
    # print("Enter the name of book")
    # Name=input()
    #
    # print("Enter the author of book")
    # Author=input()

    obj1=BookStore("Linux System Programming", "Robert Love")
    obj1.Display()

    obj2=BookStore("C Programming", "Dennis Ritchie")
    obj2.Display()



if __name__=="__main__":
    main()
