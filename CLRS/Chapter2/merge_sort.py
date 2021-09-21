def merge(arr, p, q, r):
    n1 = q-p+1
    n2 = r-q
    left = [None] * n1
    right = [None] * n2
    for i in range(0, n1):
        left[i] = arr[p+i]
    for j in range(0, n2):
        right[j] = arr[q+j+1]
    i = 0
    j = 0
    k = 0
    for k in range(p, r+1):
        if i>=n1 or j>= n2:            
            break
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1    
    while i<n1:
        arr[k] = left[i]
        i+=1
        k+=1
    while j<n2:
        arr[k] = right[j]
        j+=1
        k+=1    


def merge_sort(arr, p, r):
    if p<r:
        q = int((p+r)/2)
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)



if __name__=='__main__':
    arr = [42, 23, 1, 10, 4, 16, 73, 100]
    print("Input: " + str(arr))
    merge_sort(arr, 0, len(arr)-1)
    print("Sorted array: " + str(arr))
    