"""
[2, 7, 11, 15]

target = 26

{
    2: 0,
    7: 1
    11: 2
    15: 3
}
"""
class Solution:
    def twoSum(self, nums, target):
    #HashMap
        num_map = {}
        for i in range(len(nums)):
            num_map[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_map and i != num_map[diff]:
                return[i, num_map[diff]]
        return[]

nums = [8, 4, 5]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)
print(result)

