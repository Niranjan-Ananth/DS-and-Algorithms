def binary_search(arr, element):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + int((high-low)/2)
        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            high = mid-1
        else:
            low = mid+1
    return None

if __name__=='__main__':
    arr = [1, 23, 27, 42, 52, 67, 72, 81, 99, 100]    
    element = 23
    print("Input array: " + str(arr))
    print("Element to be searched: " + str(element))
    result = binary_search(arr, element)
    if result:
        print("Found element at index: " + str(result))
    else:
        print("Could not find element in array")
    