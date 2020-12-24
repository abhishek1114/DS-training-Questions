#User function Template for python3
class Solution:
	def numberPattern(self, N):
	    lst = []
		# code here
		for n in range(1,N+1):
		    a = ""
		    for i in range(1,n+1):
		        a+=str(i)
		    for i in range(n-1,0,-1):
		        a+=str(i)
		    lst.append(int(a))
	    print(*lst)



if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.print(Pattern(N))
