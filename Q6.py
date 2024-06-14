def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Error: The file was not found."
    except Exception as e:
        return f"An error occurred: {e}"

# Specify the filename
filename = "output.txt"

# Read the content from the file
file_content = read_from_file(filename)

# Print the content to the console
print(file_content)
