for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c=0
    l =l[::-1]
    for i in range(n-1):
        if l[i]==l[i+1]:
            print(n-i-1,l[i])
            c=1
            break
    if c==0:
        print(-1)
