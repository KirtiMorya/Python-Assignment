def concatenate_strings(str1, str2):
    return str1 + str2

def get_user_input(prompt):
    return input(prompt)

# Get the first string input from the user
first_string = get_user_input("Enter the first string: ")

# Get the second string input from the user
second_string = get_user_input("Enter the second string: ")

# Concatenate the two strings
result_string = concatenate_strings(first_string, second_string)

# Print the concatenated result
print(f"The concatenated string is: {result_string}")
