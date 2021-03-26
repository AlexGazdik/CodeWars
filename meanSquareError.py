# Complete the function that

#     accepts two integer arrays of equal length
#     compares the value each member in one array to the corresponding member in the other
#     squares the absolute value difference between those two values
#     and returns the average of those squared absolute value difference between each member pair.



def solution(array_a, array_b):
    absList =[abs(array_a[i] - array_b[i]) for i in range(len(array_a))]
    squaredList = [i**2 for i in absList]
    return sum(squaredList) / len(squaredList)
