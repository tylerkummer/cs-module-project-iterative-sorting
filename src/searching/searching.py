def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    begin_index = 0
    end_index = len(arr) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = arr[midpoint]

        if midpoint_value == target:
            return midpoint

        elif target < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return -1  # not found
