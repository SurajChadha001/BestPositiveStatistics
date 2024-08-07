def is_vowel(char):
  vowels="aeiouAEIOU"
  return char in vowels
  character=input("Enter a character:")
  if is_vowel(character):
    print(f"The character '{character}' is a vowel.")
  else:
    print(f"The character '{character}' is a consonant.")