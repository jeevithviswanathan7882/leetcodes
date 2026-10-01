class Solution:
    def secondHighest(self, s: str) -> int:
        e=[]
        num="1234567890"
        for i in s:
            if i in num and int(i) not in e:
                e.append(int(i))
        if len(e)!=0:
            e.remove(max(e))

        if len(e)==0:
            return -1
        else:
            return max(e)