def task32(array, min, max):
    res = []
    for i in range(len(array)):
        if max >= array[i] >= min:
            res.append(i)
    return res


arr =[-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]

print(task32(arr,5,14))