class Solution(object):
    def printAltNum(self, n):
        """
        :type n: int
        :rtype: None
        """
        self.printAltNumRec(n, 1)
    
    def getAltRec(self, arr, idx, res):
        if(idx >= len(arr)): return 
        res.append(arr[idx])
        self.getAltRec(arr, idx+2, res)
        
        
    def getAlt(self, arr):
        res = []
        self.getAltRec(arr, 0, res)
        return res
    
arr = [1,2,3,4,5,6,7,8,9, 10]
sol = Solution()
result = sol.getAlt(arr)
print(result)