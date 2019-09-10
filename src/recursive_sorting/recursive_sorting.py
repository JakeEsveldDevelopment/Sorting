# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    print(f"Array A {arrA}   Array B {arrB}")
    # TO-DO
    while len(arrA) != 0 and len(arrB) != 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            merged_arr.pop(0)
            arrA.pop(0)
        else:
            merged_arr.append(arrB[0])
            merged_arr.pop(0)
            arrB.pop(0)
    if len(arrA) != 0:
        for i in range(0, len(arrA)):
            merged_arr.append(arrA[i])
            merged_arr.pop(0)

    if len(arrB) != 0:
        for i in range(0, len(arrB)):
            merged_arr.append(arrB[i])
            merged_arr.pop(0)
            
    
    return merged_arr


# split into single item arrays
# compare single items and merge
# merge single item arrays into two item arrays
# compare 0th index of each, and swap into merged
# merge multi item arrays into one array
# return merged array


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    
    if len(arr) <= 1 :
        return arr

    
    left = arr[0: len(arr) // 2]
    right = arr[len(arr) // 2: len(arr)]
    sortedLeft = merge_sort(left)
    sortedRight = merge_sort(right)

    print(f"Left: {sortedLeft}     Right: {sortedRight}")
    arr = merge(sortedLeft, sortedRight)   
    

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
