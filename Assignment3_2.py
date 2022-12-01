def maximum(yaadi):
    maxi=max(yaadi)
    return maxi

def main():
    print("**** Function to display maximum number from the list ****")
    print("Enter count")
    num=int(input())

    li=[]
    for i in range(num):
        nNum = int(input())
        li.append(nNum)
    print("Numbers in a list is :", li)

    ret=maximum(li)
    print("Maximum number from a list is :", ret)

if __name__=="__main__":
    main()