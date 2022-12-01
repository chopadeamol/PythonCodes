from sys import argv

def StringInFile():
    count=0
    file=argv[1]
    file1=open(file,"r")

    String=argv[2]

    if String in file1:
        count=count+1
    print("The frequency of input string is :", count)


def main():
    StringInFile()

if __name__=="__main__":
    main()