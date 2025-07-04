def is_count(s):
    vowels = "aeiou"
    s = s.lower()
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count
n = input()
print(is_count(n))