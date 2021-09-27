import time
from utils.array_generator import random_array_generator

def selection_sort(arr):
    for i in range(0, len(arr)-1):
        min = arr[i]
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < min:
                min = arr[j]
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp


def test_selection_sort():
    print("Starting performace test")    
    n = 10000
    max_limit = 500000
    arr = random_array_generator(n, max_limit)
    start_time = time.time()
    selection_sort(arr)
    end_time = time.time()
    print("Overall time taken: " + str(end_time-start_time))
    print("Ending performace test")


if __name__=='__main__':
    arr = [42, 23, 1, 10, 4, 16, 73, 100]
    print("Input: " + str(arr))
    selection_sort(arr)
    print("Sorted array: " + str(arr))
    test_selection_sort()
    