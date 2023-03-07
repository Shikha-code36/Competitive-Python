import logging

def index_sequential_search(arr, value, jump):
    try:
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == value:
                return i
            i += jump
            if i >= n or arr[i] > value:
                break
        for j in range(max(0, i-jump+1), min(n, i+1)):
            if arr[j] == value:
                return j
        return -1
    except Exception as e:
        logging.exception("An error occurred during index sequential search: %s", e)
        return "An error occurred during index sequential search: {}".format(str(e))