def two_sum(numbers, target):
    indices = []
    l = len(numbers) - 1
    i = 0
    s = 0
    while i <= l:
        j = i + 1
        while j <= l:
            s = numbers[i] + numbers[j]
            if s == target:
                indices = (i, j)
                j = l + 1
            j = j + 1
        i = i + 1
    return indices