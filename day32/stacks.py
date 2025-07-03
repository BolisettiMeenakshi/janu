expression = "(((2)+(3)))"

stack = []
for i in expression:
    if i == '(':
        stack.append(i)
    elif i == ')':
        stack.pop()
    else:
        continue
if len(stack) == 0:
    print("Valid")
else:
    print("Invalid")