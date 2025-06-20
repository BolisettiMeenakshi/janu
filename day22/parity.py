t = int(input())
for i in range(t):
    x = int(input())
    if bin(x).count('1') % 2 == 0:
        print("Even")
    else:
        print("Odd")