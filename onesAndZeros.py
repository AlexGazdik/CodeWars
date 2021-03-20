def binary_array_to_number(arr):
    result=0
    multi=2
    for i in arr[-2::-1]:
        result+=multi*i
        multi*=2
    return result + arr[-1]
