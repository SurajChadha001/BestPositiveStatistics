def is_valid_parenthesis(expression):
  stack=[]
  mapping={"(":")","{":"}","[":"]"}
  for char in expression:
    if char in mapping:
      stack.append(char)
    elif char in mapping.values()
    if not stack or mapping[stack.pop()]!=char:
return False
return not stack
expression = "([)"
if is_valid_parenthesis(expression):
  print(f"{expression} is a valid parenthesis expression.")
else:
  print(f"{expression} is not a valid parenthesis expression.")
      