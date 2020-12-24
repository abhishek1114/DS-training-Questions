#code
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c=0
    lst=[]
    for item in l:
        if item>=0:
            c+=1
            lst.append(c)
        else:
            c=0
            lst.append(c)
    print(max(lst))
            
