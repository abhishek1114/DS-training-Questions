n = int(input())
l = list(map(int,input().split()))
while len(l)!=1:
    l.remove(max(l))
    if len(l)!=1:
        l.remove(min(l))
print(*l)
