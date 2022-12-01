import os
def CheckExist():
    print("Enter the file name you want to check exists or not")
    fd1=input()
    if os.path.exists(fd1):
        print("The file exists")
        exit()

def main():
    CheckExist()

if __name__=="__main__":
    main()