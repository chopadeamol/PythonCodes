def DisplayContents():
    print("Enter the file name you want to read")
    file=input()
    fd=open(file,"r")
    print("The contents of the file are displayed on next line........")
    print(fd.read())

def main():
    DisplayContents()

if __name__=="__main__":
    main()