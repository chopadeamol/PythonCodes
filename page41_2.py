def fibonacci():
    a = 0
    b = 1
    while True:                     # keep going
        yield a                     # report value, a, during this pass
        future = a + b
        a = b                       # this will be next value reported
        b = future                  # and subsequently this
        if a >= 50:                 # added to break the infinite loop
            break

fib = fibonacci()
print(list(fib))