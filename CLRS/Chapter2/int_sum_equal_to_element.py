from merge_sort import merge_sort

def find_integers_sum_equal_to_element(arr, element):
    merge_sort(arr, 0, len(arr)-1)
    i = 0
    j = len(arr) - 1
    while i<j:
        if arr[i] + arr[j] == element:
            return True
        elif arr[i] + arr[j] > element:
            j-=1
        else:
            i+=1
    return False


if __name__=='__main__':
    arr = [42, 23, 50, 1, 10, 4, 16, 73, 100]
    element = 741
    print("Input: " + str(arr))
    print("Find if there exists two integers whose sum equals " + str(element))
    result = find_integers_sum_equal_to_element(arr, element)
    if result:
        print("Found two integers in the array that summed up to the element")
    else:
        print("Could not find two integers in the array that summed up to the element")
    