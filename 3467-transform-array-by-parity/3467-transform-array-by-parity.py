class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        f=[]
        for i in nums:
            if i%2==0:
                f.append(0)
            else:
                f.append(1)
            f.sort()
        return f
