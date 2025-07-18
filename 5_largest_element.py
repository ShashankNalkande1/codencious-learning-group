# program to print the largest number in an array

size = int(input("Enter the size of the array = "))
data = []
for i in range(size):
    value = int(input("enter the value= ")) 
    data.append(value)

print("the array you given= ", data)

# now sorting part
max = data[0]
for i in range(size):
    if max < data[i]:
        max = data[i]

print("the largest element in the array is ", max)

# Example output:
# Enter the size of the array = 5
# enter the value= 10
# enter the value= 25
# enter the value= 7
# enter the value= 42
# enter the value= 18
# the array you given=  [10, 25, 7,]()
