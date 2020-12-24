for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    lst=[]
    for i in range(n):
        a=l[i]
        for j in range(i+1,n):
            d=abs(l[i]-l[j])
            lst.append(d)
    print(min(lst))
