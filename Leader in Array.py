def printLeaders(arr, size):
    max_from_right = arr[size - 1]
    print(max_from_right, end=' ')
    for i in range(size - 2, -1, -1):
        if max_from_right < arr[i]:
            print(arr[i], end=' ')
            max_from_right = arr[i]


# Driver function
# arr = [16, 17, 4, 3, 5, 2]
# printLeaders(arr, len(arr))


def leaders(A, N):
    lst = []
    largenum = A[N - 1]
    lst.append(largenum)
    for i in range(N - 1 - 1, -1, -1):
        if A[i] > largenum:
            lst.insert(0, A[i])
            largenum = A[i]

    return lst
