#code
for _ in range(int(input())):
    n = input().split(".")
    l = []
    for item in n:
        item = item[::-1]
        l.append(item)
    print(".".join(l))
