def find_max_subarray_brute_force(arr):
    max_sum = arr[0]
    left = 0
    right = 0
    for i in range(0, len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum > max_sum:
                max_sum = sum
                left = i
                right = j
    return left, right, max_sum

if __name__=='__main__':
    arr = [12, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    left, right, max_sum = find_max_subarray_brute_force(arr)
    print("Max subarray of sum: " + str(max_sum) + " is found between indices " + str(left) + " and " + str(right))
    pass