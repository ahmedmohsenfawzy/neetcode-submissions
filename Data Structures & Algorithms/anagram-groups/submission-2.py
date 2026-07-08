from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        dic = defaultdict(list)
        for i in strs:
            s = sorted(i)
            dic[tuple(s)].append(i)
        for i in dic.keys():
            res.append(dic[i])

        return res
                