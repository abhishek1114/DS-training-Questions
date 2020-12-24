#code
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    while(len(l)!=1):
        l.remove(max(l[0],l[-1]))
    print(*l)
