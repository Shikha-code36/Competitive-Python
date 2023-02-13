def linear_search(arr, target):
    for search in range(len(arr)):
        if arr[search] == target:
            return search
    return -1
