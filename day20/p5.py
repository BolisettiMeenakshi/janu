n = int(input())
dict = []
for i in range(n):
    list = {}
    list["name"] = input()
    list["id"] = int(input())
    dict.append(list)
print(dict)
name = input()
list = []
for i in dict:
    if name.lower() in i["name"].lower():
        list.append(i)
    #if name.lower() in ["id"].lower():
        #list.append(i)
print(list)