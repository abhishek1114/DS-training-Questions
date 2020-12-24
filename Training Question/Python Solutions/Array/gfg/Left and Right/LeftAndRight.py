for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    i = n//2
    sum1,sum2=0,0
    for p in range(i):
        sum1+=l[p]
    for j in range(i,n):
        sum2+=l[j]
    print(sum1*sum2)
