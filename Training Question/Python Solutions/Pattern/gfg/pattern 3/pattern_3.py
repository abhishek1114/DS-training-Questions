n = int(input())
k = 2*n-1
l,h=0,k-1
value = n
matrix = [[0 for i in range(k)] for j in range(k)]
for i in range(n):
    for j in range(l,h+1):
        matrix[i][j]=value
    for j in range(l+1,h+1):
        matrix[j][i]=value
    for j in range(l+1,h+1):
        matrix[h][j]=value
    for j in range(l+1,h):
        matrix[j][h]=value
    l+=1
    h-=1
    value-=1
for i in range(k):
    for j in range(k):
        print(matrix[i][j],end = " ")
    print()
