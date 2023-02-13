import logging

def shell_sort(arr):
    try:
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
        return arr
    except Exception as e:
        logging.exception("An error occurred during shell sort: %s", e)
        return []

