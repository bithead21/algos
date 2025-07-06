from typing import List


def rob(nums: List[int]) -> int:
    prev_no_rob = 0
    prev_rob = 0

    for val in nums:
        temp = max(prev_no_rob, prev_rob)
        prev_rob = prev_no_rob + val
        prev_no_rob = temp
        
    return max(prev_rob, prev_no_rob)

# 2,7,9,3,11,2,4,132,5,12,12,53,5,32,2,5

print(rob([1,2,3,1,4,3,2]))