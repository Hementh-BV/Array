def nextPermutation(self, N, arr):
    i = N - 1
    j = N - 1

    while i > 0 and arr[i - 1] >= arr[i]:
        i = i - 1

    if i == 0:
        arr.reverse()
        return arr

    while arr[j] <= arr[i - 1]:
        j = j - 1

    arr[j], arr[i - 1] = arr[i - 1], arr[j]

    arr[i:] = arr[N - 1:i - 1:-1]

    return arr
