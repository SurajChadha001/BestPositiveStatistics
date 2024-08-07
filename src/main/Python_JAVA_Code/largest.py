def find_largest(numbers):
  largest=numbers[0]
for number in numbers:
  if number>largest:
    largest=number
  return find_largest
numbers=[3,7,1,9,4]
largest_number = find_largest(numbers)
print(f"The largest number in the list is {largest_number}.")