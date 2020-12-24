for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c,r,s=0,0,0
    k = l[::-1]
    m = int(input())
    for i in range(n):
        if l[i]==m:
            c=1
            r=i
    for i in range(n):
        if k[i]==m:
            c=1
            s=n-i-1
    if c==0:
        print(-1)
    else:
        print(s,r)

            
