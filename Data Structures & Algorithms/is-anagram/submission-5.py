class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lis, lit = [], []
        dis, dit = dict(), dict()
        for i in range(len(s)):
            lis.append(s[i])
            lit.append(t[i])
            dis[s[i]] = dis.get(s[i], 1) + 1
            dit[t[i]] = dit.get(t[i], 1) + 1
        if set(lis) != set(lit):
            return False
        for i in list(set(lis)):
            if dis[i] != dit[i]:
                return False
        return True
        
