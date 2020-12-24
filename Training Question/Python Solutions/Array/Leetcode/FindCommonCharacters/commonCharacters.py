class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        p = A[0]
        lst =[]
        c=0
        for ch in p:
            for i in range(1,len(A)):
                if ch in A[i]:
                    c=0
                else:
                    c=1
                    break
            if c==0:
                lst.append(ch)
                for i in range(1,len(A)):
                    pos = A[i].index(ch)
                    A[i]=(A[i])[:pos]+(A[i])[pos+1:]
        return lst
