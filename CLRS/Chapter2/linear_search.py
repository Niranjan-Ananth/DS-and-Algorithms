def linear_search(arr, key):
    if arr is None:
        return None
    for i in range(0, len(arr)):
        if arr[i] == key:
            return i
    return None


if __name__=='__main__':
    arr = [42, 23, 1, 10, 4, 16, 73, 100]
    key = 73
    print("Find key " + str(key) + " in input array: " + str(arr))
    index = linear_search(arr, key)
    if index:
        print("Found key at index " + str(index))
    else:
        print("Could not find the element in the array")