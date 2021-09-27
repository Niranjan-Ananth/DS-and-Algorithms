import time
from utils.array_generator import random_array_generator

def insertion_sort(arr, l, r):     
    for j in range(l+1, r+1):
        i = j-1
        key = arr[j]
        while i >= l and arr[i]>key:
            arr[i+1] = arr[i]
            i-=1
        arr[i+1] = key


def merge(arr, p, q, r):
    n1 = q-p+1
    n2 = r-q
    left = [None] * n1
    right = [None] * n2
    for i in range(0, n1):
        left[i] = arr[p+i]
    for j in range(0, n2):
        right[j] = arr[q+j+1]
    i = 0
    j = 0
    k = 0
    for k in range(p, r+1):
        if i>=n1 or j>= n2:            
            break
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1    
    while i<n1:
        arr[k] = left[i]
        i+=1
        k+=1
    while j<n2:
        arr[k] = right[j]
        j+=1
        k+=1    


def merge_sort(arr, p, r, k):    
    q = int((p+r)/2)
    if q-p+1 <= k:
        insertion_sort(arr, p, q)
    else:
        merge_sort(arr, p, q, k)
    if r-q <= k:
        insertion_sort(arr, q+1, r)
    else:
        merge_sort(arr, q+1, r, k)
    merge(arr, p, q, r)


def test_merge_insertion_sort():
    print("Starting performace test")    
    n = 10000
    max_limit = 500000
    arr = random_array_generator(n, max_limit)
    start_time = time.time()
    merge_sort(arr, 0, len(arr)-1, 100)
    end_time = time.time()
    print("Overall time taken: " + str(end_time-start_time))
    print("Ending performace test")


if __name__=='__main__':
    arr = [42, 23, 1, 10, 4, 16, 73, 100, 67, 98, 33, 27, 53, 49, 89, 17]
    print("Input: " + str(arr))
    merge_sort(arr, 0, len(arr)-1, 4)
    print("Sorted array: " + str(arr))
    test_merge_insertion_sort()
    