def find_second_largest(numbers):
  if len(numbers)<2:
    return None
    sorted_numbers=sorted(numbers,reverse=True)
    return sorted_numbers[1]
numbers=[5,8,2,9,1]
second_largest=find_second_largest_sorted(numbers)
print(f"Second largest number:{second_largest}")