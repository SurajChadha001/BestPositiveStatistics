def square_list_loop(numbers):
  squared_numbers=[]
for number in numbers:
  squared_numbers.append(number*number)
return squared_numbers
numbers=[1,2,3,4,5]
squared_numbers=square_list_loop(numbers)
print(f"Squared numbers:{squared_numbers}")
