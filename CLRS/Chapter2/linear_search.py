import time
from utils.array_generator import sorted_array_generator, random_number_generator

def linear_search(arr, key):
    if arr is None:
        return None
    for i in range(0, len(arr)):
        if arr[i] == key:
            return i
    return None


def test_linear_search_performance():
    print("Starting performace test")    
    n = 100000
    max_limit = 500000
    elements_found = 0
    iterations = 1000
    arr = sorted_array_generator(n, max_limit)
    start_time = time.time()
    for i in range(0, iterations):
        element = random_number_generator(max_limit)        
        result = linear_search(arr, element)
        if result:
            elements_found += 1    
    end_time = time.time()
    print("Number of elements found: " + str(elements_found))
    print("Number of elements not found: " + str(iterations - elements_found))
    print("Overall time taken: " + str(end_time-start_time))
    print("Ending performace test")


if __name__=='__main__':
    arr = [42, 23, 1, 10, 4, 16, 73, 100]
    key = 73
    print("Find key " + str(key) + " in input array: " + str(arr))
    index = linear_search(arr, key)
    if index:
        print("Found key at index " + str(index))
    else:
        print("Could not find the element in the array")
    test_linear_search_performance()