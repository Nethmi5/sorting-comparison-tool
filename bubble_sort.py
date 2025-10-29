def bubble_sort(arr):
    n = len(arr)
    steps = 0
    data = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            steps += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data, steps
