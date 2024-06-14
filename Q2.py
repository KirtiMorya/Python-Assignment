def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Get the number from the user
num = get_number("Enter a number: ")

# Check if the number is even or odd
result = check_even_odd(num)

# Print the result
print(f"The number {num} is {result}.")
