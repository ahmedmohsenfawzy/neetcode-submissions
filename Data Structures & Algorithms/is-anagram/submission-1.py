class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        from collections import Counter
        s = dict(Counter(s))        
        t = dict(Counter(t))
        for i in s:
            try:
                if s[i] == t[i]:
                    pass
                else:
                    return False
            except KeyError:
                return False
        return True