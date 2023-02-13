import logging

def merge_sort(arr):
    try:
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            merge_sort(L)
            merge_sort(R)
            i = j = k = 0
            aux = [0] * len(arr)
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    aux[k] = L[i]
                    i += 1
                else:
                    aux[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                aux[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                aux[k] = R[j]
                j += 1
                k += 1
            for i in range(len(arr)):
                arr[i] = aux[i]
        return arr
    except Exception as e:
        logging.exception("An error occurred during merge sort: %s", e)
        return []

