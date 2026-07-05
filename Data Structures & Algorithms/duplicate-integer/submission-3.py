
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tempdict = dict()
        for i in nums:
            if i in tempdict.keys():
                return True
            else:
                tempdict[i] = 1
        return False
        
         