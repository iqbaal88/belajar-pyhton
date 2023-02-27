#pyhton slicing = untuk mengambil data secara berkelompok dari sebuah list

# python - slicing
 
numbers = list(range(0,101,2))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
 
names = ["andi", "adlin", "toni", "restu", "kamal"]
 
# [:end]
# [start:end]
# [start:end:step]
 
print(numbers[6])
print(numbers[0:6]) 
 
print(numbers[1:5])
 
print(numbers[0:10:3])
print(numbers[-1:-10:-1]) # all negative numbers
 
print(names[1:4])