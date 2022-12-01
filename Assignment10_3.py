import sys
import os

def TwoArgInput(path1, path2):
    fn1=os.path.isabs(path1)
    if fn1==False:
        path=os.path.abspath(path1)
    exist=os.path.isdir(path)

    if exist:
        for dir,subdir,file in os.walk(path1):
            print("Current folder is :"+dir)
            for subdir in dir:
                print("The subdir in :" +dir+ " is :" +subdir)
            for filename in file:
                print("The files inside " +dir+ " is :" +filename)
        print(" ")
    else:
        print("Invalid input")



def main ():
    TwoArgInput(sys.argv[1], sys.argv[2])


if __name__=="__main__":
    main()