n = int(input())
i = 1
j = n-2
for row in range(0,n):
    for col in range(0,n):
        if row==0 or row==n-1:
            print("*",end="")
        elif row==i and col ==j:
            print("*",end="")
            i+=1
            j-=1
        else:
            print(end=" ")
    print()
