# jika satu paramter range adalah semua angka yang berada di bawahnya, dan angka itu sendiri tidak termasuk.
numbers = range(50)
print(numbers)
print(list(numbers))

# python - range
 
# range(stop)
# range(start,stop)
# range(start,stop,step)
 
numbers = range(10)
print(numbers)
print(list(numbers))
 
numbers = range(50, 101)
print(numbers)
print(list(numbers))
 
numbers = range(50,101,3)
print(numbers)
print(list(numbers))
 
for i in range(10):
    print(123)