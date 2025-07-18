# learned we can use ,dict, concept, try , 
print("program to print number is even or odd without using if else")

num = int(input("Enter the number\n"))
try:
    data = 10 / (num % 2)
    print("number is  = Odd")
except ZeroDivisionError:
    print("number is = Even")

# Example output:
# Enter the number
# 4
# number is = Even
