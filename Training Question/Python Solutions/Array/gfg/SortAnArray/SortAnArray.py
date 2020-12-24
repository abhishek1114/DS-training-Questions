#User function Template for python3

def sort012(arr,n):
    # code here
    arr.sort()
    return arr


for i in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().rstrip().split()]
    sort012(arr,n)
    print(*arr)
