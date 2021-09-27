import time
import sys

def fibonacci_recursive(n):
    if n==0:
        return 0
    if n==1:
        return 1
    fib = fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    return fib

if __name__=='__main__':
    n = 30
    sys.setrecursionlimit(2000) 
    start_time = time.time()
    result = fibonacci_recursive(n)
    end_time = time.time()
    print("Fibonacci for ith number " + str(n) + " is " + str(result))
    print("Overall time taken: " + str(end_time-start_time))