def singleNumber(nums):
    a = 0
    for i in nums:
        a ^= i
    return a


def search(self, A, N):
    d = dict()
    for i in A:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    for j in d:
        if d[j] == 1:
            return j
