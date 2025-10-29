def quick_sort(arr):
    steps = [0]

    def partition(data, low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            steps[0] += 1
            if data[j] <= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1

    def sort(data, low, high):
        if low < high:
            pi = partition(data, low, high)
            sort(data, low, pi - 1)
            sort(data, pi + 1, high)

    data = arr.copy()
    sort(data, 0, len(data) - 1)
    return data, steps[0]
