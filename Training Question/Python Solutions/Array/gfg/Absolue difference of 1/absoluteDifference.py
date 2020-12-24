#code
def numCheck(n):
    rem1 = n % 10
    n = n // 10
    if not n:
        return False
    while(n):
        rem2 = n % 10
        n = n // 10
        if abs(rem2 - rem1) != 1:
            return False
        rem1 = rem2
    return True

for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    lst = []
    for item in l:
        if numCheck(item) and item<k:
            lst.append(item)
    if len(lst)==0:
        print(-1)
    else:
        print(*lst)
