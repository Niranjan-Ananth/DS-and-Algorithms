import time
from utils.array_generator import sorted_array_generator, random_number_generator

def binary_search_recursive(arr, element, low, high):
    if low > high:
        return None
    mid = low + int((high-low)/2)
    if arr[mid] == element:
        return mid
    elif arr[mid] > element:
        high = mid-1
    else:
        low = mid+1
    res = binary_search_recursive(arr, element, low, high)
    return res


def test_binary_search_recursive_performance():
    print("Starting performace test")    
    n = 100000
    max_limit = 500000
    elements_found = 0
    iterations = 10000
    arr = sorted_array_generator(n, max_limit)
    start_time = time.time()
    for i in range(0, iterations):
        element = random_number_generator(max_limit)        
        result = binary_search_recursive(arr, element, 0, len(arr)-1)
        if result:
            elements_found += 1
    end_time = time.time()
    print("Number of elements found: " + str(elements_found))
    print("Number of elements not found: " + str(iterations - elements_found))
    print("Overall time taken: " + str(end_time-start_time))
    print("Ending performace test")


if __name__=='__main__':
    arr = [1, 23, 27, 42, 52, 67, 72, 81, 99, 100]    
    element = 100
    print("Input array: " + str(arr))
    print("Element to be searched: " + str(element))
    result = binary_search_recursive(arr, element, 0, len(arr)-1)
    if result:
        print("Found element at index: " + str(result))
    else:
        print("Could not find element in array")
    test_binary_search_recursive_performance()
    