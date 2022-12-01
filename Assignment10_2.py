import os
import sys

def cwd(path1, path2):
    rootdir=os.path.isdir(path1,path2)
    if rootdir:
        for folder, subfolder, file in os.walk(path1):
            for fold in folder:
                print(" Subfolder inside folder is :" +fold, end='')
            for filename in file:
                print(" File inside " +folder+ " is : " +filename)
                if filename.endswith(path2):
                    print(filename)
            print('')

    else:
        print("Invalid path")

def main():
    cwd(sys.argv[1], sys.argv[2])


if __name__=="__main__":
    main()