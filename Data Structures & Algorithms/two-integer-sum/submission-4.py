class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        for k in range(len(nums)):
            diff = target - nums[k]
            if diff in dic:
                return [dic[diff], k]
            else:
                dic[nums[k]] = k

