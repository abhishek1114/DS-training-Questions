#User function Template for python3

class Solution:
    def printPattern(self, N):
    	#code here
    	lst = []
    	for i in range(1,N+1):
    	    lst.append(i*"*")
    	print(*lst)
        return

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.print(Pattern(N))
