def merge_sort(arr):
    steps = [0]  # list to allow mutation inside recursion

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            steps[0] += 1
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    def divide(data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = divide(data[:mid])
        right = divide(data[mid:])
        return merge(left, right)

    sorted_arr = divide(arr)
    return sorted_arr, steps[0]
