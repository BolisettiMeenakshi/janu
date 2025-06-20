t = int(input())
for i in range(t):
    x = list(map(int,input().strip().split()))
    max_no = max(x)
    x.remove(max_no)
    second_max = max(x)
    print(second_max)