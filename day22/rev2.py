t = int(input())
for i in range(t):
    x = list(map(int,input().strip().split()))
    rev_list = x[::-1]
    print(rev_list)