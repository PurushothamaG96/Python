class Solution(object):
  
    def findMax(self, nums):
        return findMaxByRec(nums, 0)
        
    
def findMaxByRec(nums, i):
    if(i >= len(nums)-1): return nums[i]
    
    lastI = findMaxByRec(nums, i+1)
    return max(lastI, nums[i])

nums = [9, 8, 7, 10, 20, 123]
sol = Solution()
result = sol.findMax(nums)
print(result)
    
