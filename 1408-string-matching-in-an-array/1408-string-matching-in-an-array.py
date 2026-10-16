class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        f=[]
        for  i in words:
            for j in words:
                if i==j:
                    continue
                elif i in j:
                    f.append(i)
        f=set(f)
        f=list(f)
        return f