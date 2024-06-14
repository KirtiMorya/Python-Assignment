def get_string_length(s):
    return len(s)

def get_user_input(prompt):
    return input(prompt)

# Get the string input from the user
user_input = get_user_input("Enter a string: ")

# Get the length of the string
string_length = get_string_length(user_input)

# Print the length of the string
print(f"The length of the string is {string_length}.")
