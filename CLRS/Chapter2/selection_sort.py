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


if __name__=='__main__':
    arr = [42, 23, 1, 10, 4, 16, 73, 100]
    print("Input: " + str(arr))
    selection_sort(arr)
    print("Sorted array: " + str(arr))
    