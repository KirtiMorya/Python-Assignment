def get_string(prompt):
    return input(prompt)

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Content successfully written to {filename}")

# Get the string input from the user
user_input = get_string("Enter a string to write to the file: ")

# Specify the filename
filename = "output.txt"

# Write the input to the file
write_to_file(filename, user_input)
