def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def get_non_negative_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num < 0:
                print("Please enter a non-negative integer.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Get the number from the user
num = get_non_negative_integer("Enter a non-negative integer: ")

# Calculate the factorial
factorial_result = factorial(num)

# Print the result
print(f"The factorial of {num} is {factorial_result}.")
