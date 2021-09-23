import time
from array_generator import random_array_generator
import sys

def insertion_sort_recursive(arr, n):
    if n==0:
        return
    insertion_sort_recursive(arr, n-1)
    key = arr[n]
    i=n-1
    while i>=0 and arr[i]>key:
        arr[i+1] = arr[i]
        i-=1
    arr[i+1] = key


def test_insertion_sort_recursive():
    print("Starting performace test")
    sys.setrecursionlimit(1500) 
    n = 1000
    max_limit = 500000
    arr = random_array_generator(n, max_limit)
    start_time = time.time()
    insertion_sort_recursive(arr, len(arr)-1)
    end_time = time.time()
    print("Overall time taken: " + str(end_time-start_time))
    print("Ending performace test")


if __name__=='__main__':
    arr = [42, 23, 1, 10, 4, 16, 73, 100]
    print("Input: " + str(arr))
    insertion_sort_recursive(arr, len(arr)-1)
    print("Sorted Ascending: " + str(arr))
    test_insertion_sort_recursive()
