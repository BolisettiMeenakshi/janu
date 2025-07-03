expression = "[{([2 + 3]{6 - 1}{5 + 4})}]"

stack = []
for i in expression:
    if i == '(' or i == '{' or i == '[':
        stack.append(i)
    elif i == ')' or i == '}' or i == ']':
        if len(stack) != 0:
            stack.pop()
    else:
        continue
if len(stack) == 0:
    print("Valid")
else:
    print("Invalid")