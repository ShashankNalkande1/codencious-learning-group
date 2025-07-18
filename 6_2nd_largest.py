# program to print the 2nd largest element in the array
data = []

size = int(input("program to print the 2nd largest Element in the array= "))
for i in range(size):
    value = int(input("Enter the value"))
    data.append(value)

print(data)
data.sort()
print("the second largest element in the array is", data[-2])

# Example output:
# program to print the 2nd largest Element in the array= 5
# Enter the value10
# Enter the value25
# Enter the value7
# Enter the value42
# Enter the value18
# [10, 25, 7, 42, 18]
# the second largest element in the array is 25
