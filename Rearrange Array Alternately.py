def rearrange(self, arr, n):
    if n == 1:
        return arr
    res = []
    a, b = 0, n - 1
    while a < b:
        res.append(arr[b])
        b -= 1
        res.append(arr[a])
        a += 1
    if n % 2 != 0:
        m = (n + 1) // 2
        res.append(arr[m - 1])
    arr[:] = res[:]
