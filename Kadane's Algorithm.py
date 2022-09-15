def maxSubArray(self, nums):
    maxSub = nums[0]
    curSub = 0

    for n in nums:
        if curSub < 0:
            curSub = 0

        curSub += n
        maxSub = max(maxSub, curSub)

    return maxSub
