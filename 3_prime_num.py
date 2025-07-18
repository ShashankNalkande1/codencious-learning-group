# program to print the prime using functions
# learned the concept of prime when % by this then never give 0 and it is always greater than 1 

def prime_function():
    size = int(input("Enter the size of the array = "))
    data = []
    for i in range(size):
        value = int(input("Enter value: "))
        data.append(value)

    prime_values = []
    for num in data:
        if num > 1:
            is_prime = True
            for i in range(2, num):  # no sqrt used
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_values.append(num)

    if len(prime_values) == 0:
        return "Empty list"
    else:
        return prime_values

# Call and print
print(prime_function())

# Example output:
# Enter the size of the array = 5
# Enter value: 4
# Enter value: 7
# Enter value: 9
# Enter value: 11
# Enter value: 15
# [7, 11]
