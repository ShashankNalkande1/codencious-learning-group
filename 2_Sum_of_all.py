# write a program that prints the sum of all numbers in an array

print("Program to print the sum of all numbers in an array = ")
size = int(input("Enter the size of the array = "))
sum = 0
for i in range(size):
    value = int(input("Enter the value = "))
    sum = value + sum

print("The sum of all array of size", size, "is =", sum)

# Example output:
# Program to print the sum of all numbers in an array = 
# Enter the size of the array = 4
# Enter the value = 5
# Enter the value = 10
# Enter the value = 15
# Enter the value = 20
# The sum of all array of size 4 is = 50
