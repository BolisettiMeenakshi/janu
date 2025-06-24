char = input()
for i in range(0,26):
    printed_val = (ord(char) + i)
    print( chr(printed_val), end=" ")
print()
