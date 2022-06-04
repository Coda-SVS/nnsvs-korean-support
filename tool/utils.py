def list_chunk(lst, n: int):
    count = len(lst) // n
    result = [lst[i * count : i * count + count] for i in range(0, n)]

    if isinstance(lst, list):
        for temp in lst[count * n :]:
            result[n - 1].append(temp)
    else:
        for temp in lst[count * n :]:
            result[n - 1] += temp
    return result
