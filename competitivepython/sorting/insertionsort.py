def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        target = arr[i]
        j = i - 1
        while j >= 0 and target < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = target
    return arr
