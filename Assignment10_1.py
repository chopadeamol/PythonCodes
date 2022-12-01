import os
from sys import *

def SearchText(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    #path=os.path.exists(folder)
    if exists:
        for foldername, subfolder, filename in os.walk(path):
            print("current folder is :", +foldername)

            for subf in subfolder:
                print("Subfolder of"+foldername+"is :",subf)

            for file in filename:
                print("file inside :"+foldername+ "is :",+file)

            print('')
    else:
        print("Invalid path")


def main ():
    print("The length of the arguments passed", (len(argv)-1))
    print("The name of script :",argv[0])
    if (len(argv) !=3):
        print("Invalid number of arguments")
        exit()

    if argv[1]=="-u" or argv[1]=="-U":
        print("Usage : DirectoryFileSearch.py 'Demo' '.txt' ")
        exit()

    if argv[1]=="-h" or argv[1]=="-H":
        print("This script is used to search a .txt extension file in the directory")
        exit()

    try:
        SearchText(argv[1])
    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception:
        print("Error : Invalid input")


if __name__=="__main__":
    main()