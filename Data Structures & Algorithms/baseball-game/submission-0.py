class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lis = []
        for index, i in enumerate(operations):
            if i == '+':
                lis.append(int(lis[-2]) + int(lis[-1]))
            elif i == 'D':
                lis.append(int(lis[-1]) * 2)
            elif i == 'C':
                lis.pop()
            else:
                lis.append(int(i))
        return sum(lis)