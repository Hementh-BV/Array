def majorityElement(self, nums):
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1
        if d[i] > len(nums) // 2:
            return i


def majorityElement(self, arr, N):
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    v = list(d.values())
    k = list(d.keys())
    res = k[v.index(max(v))]
    if res == 1:
        return -1
    return res
