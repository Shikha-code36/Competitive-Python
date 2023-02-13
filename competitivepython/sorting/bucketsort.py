import logging

def bucket_sort(arr):
    try:
        n = len(arr)
        max_val = max(arr)
        bucket = []
        for i in range(n):
            bucket.append([])
        for i in arr:
            index_b = int(n * i / max_val)
            if index_b != n:
                bucket[index_b].append(i)
            else:
                bucket[n - 1].append(i)
        for i in range(n):
            bucket[i] = sorted(bucket[i])
        result = []
        for i in range(n):
            result = result + bucket[i]
        return result
    except Exception as e:
        logging.exception("An error occurred during bucket sort: %s", e)
        return "An error occurred during bucket sort: {}".format(str(e))
