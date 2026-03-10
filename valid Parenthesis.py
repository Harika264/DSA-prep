s = input()

stack = []
pairs = {')':'(', '}':'{', ']':'['}

for i in s:
    if i in "({[":
        stack.append(i)
    else:
        if not stack or stack[-1] != pairs[i]:
            print("Invalid")
            break
        stack.pop()
else:
    print("Valid")
