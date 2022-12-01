def sum(values):
    total = 0
    for v in values:
        total = total + v
    return total

def main():
    li = [1,2,3,4,5]
    addition = sum(li)
    print("Sum of the values inside input list is:",addition)
main()