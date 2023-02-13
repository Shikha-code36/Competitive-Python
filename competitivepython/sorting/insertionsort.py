import logging

def insertion_sort(arr):
    try:
        n = len(arr)
        for i in range(1, n):
            target = arr[i]
            j = i - 1
            while j >= 0 and target < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = target
        return arr
    except Exception as e:
        logging.exception("An error occurred during insertion sort: %s", e)
        return []

