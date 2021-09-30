def find_max_subarray_linear(arr):
    max_sum = arr[0]
    current_sum = 0
    left = 0
    right = 0
    max_left = 0
    max_right = 0
    for i in range(0, len(arr)):        
        if current_sum + arr[i]  > arr[i]:
            current_sum = current_sum + arr[i]
            right = i
        else:
            current_sum = arr[i]
            left = i
            right = i
        if current_sum > max_sum:
            max_sum = current_sum
            max_left = left
            max_right = right 
    return max_left, max_right, max_sum

if __name__=='__main__':
    arr = [12, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    left, right, max_sum = find_max_subarray_linear(arr)
    print("Max subarray of sum: " + str(max_sum) + " is found between indices " + str(left) + " and " + str(right))
    pass