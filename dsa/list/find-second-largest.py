class Solution(object):
    def findSecondLargestNum(self, nums):
        max = nums[0]
        secMax = -1
        length = len(nums)
        for i in range(1, length):
            currentNum = nums[i]
            print(currentNum)
            if currentNum > max:
                secMax = max
                max = currentNum
            if(currentNum < max and currentNum > secMax):
                secMax = currentNum
        return secMax
    
nums = [12, 35, 1, 10, 34, 1]
sol = Solution()
result = sol.findSecondLargestNum(nums)
print(result)
                