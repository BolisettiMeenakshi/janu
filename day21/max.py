t = int(input())
for i in range(t):
    n = int(input())
    list1 = list(map(int,input().strip().split()))
    max_value = list1[0]
    for j in range(1, n):
       if list1[j] > max_value:
            max_value = list1[j]
    print(max_value)