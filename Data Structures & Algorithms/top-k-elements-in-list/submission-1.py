class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = Counter(nums)
        lis = []
        res = []
        for v in n.values():
            lis.append(v)
        lis = sorted(lis)
        for i, v in n.items():
            print(i)
            print(f"{v}-")
            print(lis)
            if v in lis[-k:]:
                print(f"{i}--")
                res.append(i)
        return res
