#code
for _ in range(int(input())):
    n = input()
    l = len(n)
    i=0
    while i<l-1:
        print(n)
        n = n.replace(n[i],".",1)
        i+=1
    print(n)
