for i in range(int(input())):
    n = int(input())
    def recpositive(n,lst,p):
        if n<0:
            c=n
            lst.append(n)
            return recnegative(c,lst,p)
        else:
            lst.append(n)
            n-=5
            return recpositive(n,lst,p)
    def recnegative(n,lst,p):
        # print(lst,n,p)
        if n==p:
            print(*lst)
        else:
            n+=5
            lst.append(n)
            return recnegative(n,lst,p)
    lst = []
    p=n
    recpositive(n,lst,p)
