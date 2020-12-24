#User function Template for python3
class Solution:
	def removeDups(self, S):
		# code here
		l = []
		for i in s:
		    if i not in l:
		        l.append(i)
	    return "".join(l)

if __name__=='__main__':
    T=int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)
