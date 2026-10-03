class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count=0
        l=[]
        for i in permutations(digits,3):
            k=int("".join(map(str,i)))
            if k>99 and k%2==0 and k not  in l:
                l.append(k)
                count+=1
                print(k)
        return count