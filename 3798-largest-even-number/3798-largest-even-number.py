class Solution:
    def largestEven(self, s: str) -> str:
        f=int(s)
        if f%2==0:
            return s
        else:
            q=list(s)
            k=True
            while k==True:
                q=q[:-1]
                e=""
                print(q)
                for i in q:
                    e+=i
                print(e)
                if len(e)>0:
                    z=int(e)
                    if z%2==0:
                        k=False
                        return e
                    else:
                        q=list(e)
                        k=True
                else:
                    return e