numbers = [8, 7, 5, 4, 6, 4, 5, 3, 2, 1, 10]
 
numbers_summary = 0
 
for n in numbers:
    numbers_summary = numbers_summary + n
 
print(f"The sum of numbers is {numbers_summary}")
print(f"The sum of numbers is {sum(numbers)}")
