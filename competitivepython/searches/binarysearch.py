import logging

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    try:
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    except Exception as e:
        logging.exception("An error occurred during binary search: %s", e)
        return -1
