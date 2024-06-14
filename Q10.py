def convert_to_uppercase(s):
    return s.upper()

def get_user_input(prompt):
    return input(prompt)

# Get the string input from the user
user_input = get_user_input("Enter a string: ")

# Convert the string to uppercase
uppercase_string = convert_to_uppercase(user_input)

# Print the uppercase string
print(f"The uppercase string is: {uppercase_string}")
