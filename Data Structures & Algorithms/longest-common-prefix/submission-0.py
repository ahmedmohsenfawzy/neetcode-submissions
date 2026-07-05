class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new_str = strs[0]
        for i in strs[1:]:
            if len(i) < len(new_str):
                new_str = new_str[:len(i)]
            for index, j in enumerate(new_str):
                if i[index] == j:
                    continue
                else:
                    new_str = new_str[:index]
                
        return new_str

