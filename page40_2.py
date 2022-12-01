# Implementation of generator for calculating factors
import time


def factors(n):                     #generator that computes factors
    for k in range(1, n+1):         
        if n % k == 0:              # divides evenly, thus k is a factor
            yield k                 # yield this factor as next result

def main():
    start = time.time()

    n = int(input("Enter a number(generator): "))
    fact = factors(n)
    print(list(fact))
    
    end = time.time()
    TimeTaken = end-start
    print("Time required to execute a program is: ", TimeTaken)
main()
