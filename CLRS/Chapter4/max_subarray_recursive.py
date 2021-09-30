def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = -10000
    sum = 0
    left = 0
    right = 0
    for i in range(mid, low-1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            left = i
    right_sum = -10000
    sum = 0
    for i in range(mid+1, high+1):
        sum += arr[i]
        if sum > right_sum:
            right_sum = sum
            right = i
    return left, right, left_sum+right_sum

def find_max_subarray_recursive(arr, low, high):
    if low==high:
        return low, high, arr[low]
    mid = int((low+high)/2)
    left_low, left_high, left_sum = find_max_subarray_recursive(arr, low, mid)
    right_low, right_high, right_sum = find_max_subarray_recursive(arr, mid+1, high)
    cross_low, cross_high, cross_sum  = find_max_crossing_subarray(arr, low, mid, high)
    if left_sum > right_sum and left_sum > cross_sum:
        return left_low, left_high, left_sum
    if right_sum > left_sum and right_sum > cross_sum:
        return right_low, right_high, right_sum
    return cross_low, cross_high, cross_sum

if __name__=='__main__':
    arr = [12, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    left, right, max_sum = find_max_subarray_recursive(arr, 0, len(arr)-1)
    print("Max subarray of sum: " + str(max_sum) + " is found between indices " + str(left) + " and " + str(right))
