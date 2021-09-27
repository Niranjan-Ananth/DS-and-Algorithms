import time

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    a = 0
    b = 1
    fib = 1
    for i in range(0, n-1):        
        fib = a + b
        temp = b
        b = fib
        a = temp
    return fib

if __name__=='__main__':
    n = 100
    start_time = time.time()
    result = fibonacci(n)
    end_time = time.time()
    print("Fibonacci for ith number " + str(n) + " is " + str(result))
    print("Overall time taken: " + str(end_time-start_time))