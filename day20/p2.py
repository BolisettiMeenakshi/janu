list = list(map(str,input().split(" ")))
print(list)
keyword = input()
list1 = []
for i in list:
    if keyword.lower() in i.lower():
        list1.append(i)
    
print(list1)