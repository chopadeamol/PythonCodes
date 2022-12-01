from sys import *
import os

def compare():
    file1=argv[1]
    # if os.path.isfile(file1):
    #     print("File1 exists")
    file11=open(file1,"r")

    file2=argv[2]
    # if os.path.isfile(file2):
    #     print("file2 exists")
    file22=open(file2, "r")

    for f1 in file11:
        for f2 in file22:
            if f1==f2:
                print("Success")
            else:
                print("Failure")

def main():
    compare()


if __name__=="__main__":
    main()