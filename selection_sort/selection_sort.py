def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        # minimum element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
