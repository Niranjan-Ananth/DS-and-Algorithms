import time
from utils.array_generator import random_array_generator

def insertion_sort_ascending(arr):
    if arr is None:
        return None    
    for j in range(1, len(arr)):
        i = j-1
        key = arr[j]
        while i >= 0 and arr[i]>key:
            arr[i+1] = arr[i]
            i-=1
        arr[i+1] = key
    return arr
    

def insertion_sort_descending(arr):
    if arr is None:
        return None
    for j in range(1, len(arr)):
        i = j-1
        key = arr[j]
        while i>=0 and arr[i]<key:
            arr[i+1] = arr[i]
            i-=1
        arr[i+1] = key
    return arr


def test_insertion_sort_ascending_performance():
    print("Starting performace test")
    n = 10000
    max_limit = 500000
    arr = random_array_generator(n, max_limit)
    start_time = time.time()
    insertion_sort_ascending(arr)
    end_time = time.time()
    print("Overall time taken: " + str(end_time-start_time))
    print("Ending performace test")

if __name__=='__main__':
    arr_a = [42, 23, 1, 10, 4, 16, 73, 100]
    arr_b = arr_a[:]  # Copying array a into a new array for the descending sort
    print("Input: " + str(arr_a))
    insertion_sort_ascending(arr_a)
    insertion_sort_descending(arr_b)
    print("Sorted Ascending: " + str(arr_a))
    print("Sorted Descending: " + str(arr_b))
    test_insertion_sort_ascending_performance()  
