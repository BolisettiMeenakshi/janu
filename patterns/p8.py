x = int(input())
y = int(input())
for i in range(1, x + 1):
    for j in range(i):
        print(y, end = " ")
        y += 1
    print()