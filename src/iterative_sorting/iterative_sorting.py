# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x



        # TO-DO: swap
        current = arr[i]
        smallest = arr[smallest_index]
        arr[i] = smallest
        arr[smallest_index] = current


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(1, len(arr)):
            val1 = arr[i - 1]
            val2 = arr[i]
            if val2 < val1:
                arr[i - 1] = val2
                arr[i] = val1
                swapped = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr