# python - indexing = mengambil salah satu data dari list
# positive indexing = starts from 0, left to right
# negative indexing = starts from -1, right to left
 
numbers = range(0,51,3)
names = ["andi", "adlin", "toni", "restu", "kamal"]
print(list(numbers))
 
print(numbers[0])
print(numbers[15])
print(numbers[16])
# print(numbers[17]) # error, out of range
 
print(numbers[-3])
 
print(names[2])
print(names[-1])
# print(names[-13]) # error, out of range