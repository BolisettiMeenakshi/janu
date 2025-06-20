t = int(input())
for i in range(t):
    x = list(map(int,input().strip().split()))
    y = int(input())
    if y in x:
        print("yes")
    else:
        print("no")