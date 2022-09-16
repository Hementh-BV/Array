# Brute Force
def longestConsecutive(self, nums: List[int]) -> int:
    max_len = 0
    num_set = set(nums)
    for num in nums:
        curr_num = num
        curr_len = 1
        while curr_num + 1 in num_set:
            curr_num += 1
            curr_len += 1
        max_len = max(max_len, curr_len)
    return max_len

# Best Solution
def longestConsecutive(self, nums):

    num_set = set(nums)

    longest_sequence = 0
    for num in nums:
        if num - 1 in num_set:
            continue
        current_length = 1
        while num + 1 in num_set:
            num += 1
            current_length += 1
        longest_sequence = max(longest_sequence, current_length)
    return longest_sequence
