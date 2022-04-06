##### selection sort implementation #####
import random


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        i_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[i_min]:
                i_min = j
        if not (i == i_min):
            arr[i], arr[i_min] = arr[i_min], arr[i]


###############################################################


##### insertion sort implementation #####
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i
        while j > 0 and arr[j - 1] > key:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = key


###############################################################


##### merge sort implementation #####
def merge(arr, al, ar):
    """merges al & ar in arr"""
    len_left = (len(al))
    len_right = (len(ar))
    left_counter = right_counter = arr_counter = 0

    while left_counter < len_left and right_counter < len_right:
        if al[left_counter] < ar[right_counter]:
            arr[arr_counter] = al[left_counter]
            left_counter += 1
        else:
            arr[arr_counter] = ar[right_counter]
            right_counter += 1
        arr_counter += 1

    while left_counter < len_left:
        arr[arr_counter] = al[left_counter]
        left_counter += 1
        arr_counter += 1

    while right_counter < len_right:
        arr[arr_counter] = ar[right_counter]
        right_counter += 1
        arr_counter += 1


def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        merge_sort(left_arr)
        merge_sort(right_arr)
        merge(arr, left_arr, right_arr)


###############################################################


##### quick sort implementation #####
def partition(arr, start, end):
    """ partitioning assuming pivot at last index """
    pivot_value = arr[end]
    s = start - 1  # indicates where the smaller elements end in the list
    i: int  # iterator over items
    for i in range(start, end):
        if arr[i] <= pivot_value:
            s += 1
            arr[s], arr[i] = arr[i], arr[s]
    arr[s + 1], arr[end] = arr[end], arr[s + 1]  # placing the pivot in the proper index
    return s + 1  # pivot current index


def partition_random_pivot(arr, start, end):
    pivot = random.randrange(start, end + 1, 1)  # choosing random pivot
    arr[pivot], arr[end] = arr[end], arr[pivot]  # placing the pivot at the last index for the defined partition
    return partition(arr, start, end)


def quick_sort(arr, start, end):
    if start < end:
        p = partition_random_pivot(arr, start, end)
        quick_sort(arr, start, p-1)
        quick_sort(arr, p+1, end)
