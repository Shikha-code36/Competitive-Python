import logging

def bubble_sort(arr):
    try:
        length = len(arr)
        for i in range(length):
            for j in range(0, length-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    except Exception as e:
        logging.exception("An error occurred during bubble sort: %s", e)
        return "An error occurred during bubble sort: {}".format(str(e))

