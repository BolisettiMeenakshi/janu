str1 = input()
str2 = input()

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()
print(sorted(str1) == sorted(str2))