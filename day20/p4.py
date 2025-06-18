n = int(input())
dict = []
for i in range(n):
    list = {}
    list["name"] = input()
    list["id"] = int(input())
    dict.append(list)
print(dict)