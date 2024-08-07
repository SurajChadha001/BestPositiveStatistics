def is_palindrome(text):
  text = text.lower().replace("","")
  return text == text[::-1]
  text="Race car"
  if is_palindrome(text):
    print(f"{text} is a palindrome.")
  else:
    print(f"{text}is not a palindrome.")
    