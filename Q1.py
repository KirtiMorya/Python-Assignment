def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Get the first number
num1 = get_number("Enter the first number: ")

# Get the second number
num2 = get_number("Enter the second number: ")

# Calculate the sum
sum_result = num1 + num2

# Print the result
print(f"The sum of {num1} and {num2} is {sum_result}.")
