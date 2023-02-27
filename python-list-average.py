from statistics import mean
 
numbers = [8, 7, 5, 4, 6, 4, 5, 3, 2, 1, 10]
 
numbers_sum = sum(numbers) # total jumlah
numbers_length = len(numbers) # banyak data
numbers_average = numbers_sum/numbers_length # rata2
 
#print(f"average of numbers is {numbers_average}")
print(f"average of numbers is {mean(numbers)}")