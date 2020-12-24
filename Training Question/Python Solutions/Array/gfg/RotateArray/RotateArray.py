#code
for _ in range(int(input())):
    n,k = map(int,input().split())
    lst = []
    l = list(map(int,input().split()))
    p = l[:k]
    lst = l[k:]
    lst.extend(p)
    print(*lst)
