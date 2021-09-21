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


if __name__=='__main__':
    arr = [42, 23, 1, 10, 4, 16, 73, 100]
    print("Input: " + str(arr))
    insertion_sort_recursive(arr, len(arr)-1)
    print("Sorted Ascending: " + str(arr))
