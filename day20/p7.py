def slug_generator(string):
    title = (string.lower()).replace(" ", "-")

    return title

title = input()
result = slug_generator(title)
print(result)