def add_binary_integers(arr_a, arr_b):
    n = len(arr_a)
    arr_c = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        sum = arr_a[i] + arr_b[i] + arr_c[i+1]
        arr_c[i+1] = int(sum % 2)
        arr_c[i] = int(sum / 2)
    return arr_c


def add_hexadecimal_integers(arr_a, arr_b):  # Extension on the problem
    n = len(arr_a)
    arr_c = [0] * (n + 1)
    arr_a = __convert_hex_arr_to_int_arr(arr_a)
    arr_b = __convert_hex_arr_to_int_arr(arr_b)
    for i in range(n-1, -1, -1):
        sum = arr_a[i] + arr_b[i] + arr_c[i+1]
        arr_c[i+1] = int(sum % 16)        
        arr_c[i] = int(sum / 16)
    for i in range(0, n+1):
        if arr_c[i] > 9:
            arr_c[i] = chr(ord('A')+ (arr_c[i] - 10))
    return arr_c


def __convert_hex_arr_to_int_arr(arr):
    for i in range(len(arr)):
        if isinstance(arr[i], str):
            ascii_value = ord(arr[i])
            int_representation = 9 + (ascii_value - 64)
            arr[i] = int_representation
    return arr


if __name__=='__main__':
    arr_a = [1, 0, 1]
    arr_b = [1, 0, 1]
    print("Add binary intergers represented as arrays " + str(arr_a) + " and " + str(arr_b))
    arr_c = add_binary_integers(arr_a, arr_b)
    print("Added binary integer: " + str(arr_c))

    arr_a = ['F', 0, 9]
    arr_b = ['C', 'A', 1]
    print("Add hexadecimal intergers represented as arrays " + str(arr_a) + " and " + str(arr_b))
    arr_c = add_hexadecimal_integers(arr_a, arr_b)
    print("Added hexadecimal integer: " + str(arr_c))
    