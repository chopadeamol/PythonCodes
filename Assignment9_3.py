from sys import argv

def createCopy():
    print("Accepting the input from command line arguments to create file")

    file=argv[1]
    file1=open(file,"x")
    print("File created successfully")

    file2=open("Demo.txt", "r")
    for line in file2:
        file1.write(line)
    print("The contents has been copied from existing file to the newly created file")

def main():
    createCopy()

if __name__=="__main__":
    main()