import logging

def selection_sort(arr):
    try:
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    except Exception as e:
        logging.exception("An error occurred during selection sort: %s", e)
        return []
