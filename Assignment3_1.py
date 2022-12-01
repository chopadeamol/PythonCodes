def addition(list):
    add=0
    for i in range(len(list)):
        add=add+list[i]
    return add

def main():
    print("Accept N numbers from user store in list and return addition")
    print("How much N numbers you want to store?")

    no=int(input())
    nlist=[]

    print("Please enter the N numbers you want to store in list")

    for i in range(no):
        nlist.append(int(input()))
    print("Your entered N numbers are :",nlist)

    ret=addition(nlist)
    print("Addition of entered number is :", ret)

if __name__=="__main__":
    main()