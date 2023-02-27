number = int(input("Enter a number to be multiplied: "))
loop = int(input("How many loops? "))
 
for n in range(1, loop+1): # range(0,10) = [0,1,2,3,4,5,6,7,8,9]
    result = number * n
    print(f"{number} x {n} = {result}")