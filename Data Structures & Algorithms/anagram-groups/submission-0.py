class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = {}
        for i in strs:
            k = "".join(sorted(i))
            if k in dic:
                dic[k].append(i)
            else:
                dic[k] = [i]
        for l in dic:
            res.append(dic[l])
        return res