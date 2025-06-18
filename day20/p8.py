def slug_generator(name : str):
    name = name.lower()
    name = list(name)
    result = " "
    for i in range(0,len(name)):
        if name[i].isalnum():
            result += name[i]
        elif name[i] == " ":
            result += "-"
        else:
            continue
title = input()
result = slug_generator(title)
print(result)