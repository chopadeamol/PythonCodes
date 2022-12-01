import time

def factors(n):                 # Traditional function that computes factors
    results = []                # store factors in list
    for k in range(1, n+1): 
        if n % k == 0:          # divides evenly, thus k is a factor
            results.append(k)   # add k to the list of factors
    return results              # return the entire list

def main():
    start = time.time()

    n = int(input("Enter a number: "))
    fact = factors(n)
    print(fact)

    end = time.time()
    TimeTaken = end-start
    print("Time taken to execute a program is: ",TimeTaken)

main()
