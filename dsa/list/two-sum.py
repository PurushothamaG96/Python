class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in numDict:
                return [numDict[rem], i]
            numDict[nums[i]] = i

# Sample run
nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))
