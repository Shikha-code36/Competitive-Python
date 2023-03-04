import logging

def linear_search(arr, target):
    try:
        for search in range(len(arr)):
            if arr[search] == target:
                return search
        return -1
    except Exception as e:
        logging.exception("An error occurred during linear search: %s", e)
        return "An error occurred during linear search: {}".format(str(e))

