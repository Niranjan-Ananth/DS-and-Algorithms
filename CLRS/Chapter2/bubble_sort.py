def bubble_sort(arr, l, r):       
    for i in range(l+1, r):
        for j in range(r, i-1, -1):
            if arr[j] < arr[j-1]:
                temp = arr[j-1]
                arr[j-1] = arr[j]        
                arr[j] = temp


if __name__=='__main__':
    arr = [42, 23, 1, 10, 4, 16, 73, 100, 67, 98, 33, 27, 53, 49, 89, 17]
    print("Input: " + str(arr))
    bubble_sort(arr, 0, len(arr)-1)
    print("Sorted array: " + str(arr))
    