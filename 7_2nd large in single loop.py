# compiler error getting but the problem is solved 
print("program to print the second largest in the array in single loop")

size = int(input("Enter the size of the array: "))
data = []

for i in range(size):
    value = int(input("enter the value: "))
    data.append(value)

if size < 2:
    print("Need at least 2 elements to find second largest.")
else:
    print("your array:", data)

    # Initialize safely
    if data[0] > data[1]:
        biggest = data[0]
        second_largest = data[1]
    else:
        biggest = data[1]
        second_largest = data[0]

    for i in range(2, size):  # Start from 3rd element
        if data[i] > biggest:
            second_largest = biggest
            biggest = data[i]
        elif data[i] > second_largest and data[i] != biggest:
            second_largest = data[i]

    print("the second largest element:", second_largest)

# Example output:
# program to print the second largest in the array in single loop
# Enter the size of the array: 5
# enter the value: 10
# enter the value: 50
# enter the value: 30
# enter the value: 40
# enter the value: 20
# your array: [10, 50, 30, 40, 20]
# the second largest element: 40
