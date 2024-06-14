def check_substring_in(full_string, substring):
  """Checks if a substring is present in a given string using the 'in' operator.

  Args:
      full_string: The full string to search within.
      substring: The substring to search for.

  Returns:
      True if the substring is found in the full string, False otherwise.
  """

  return substring in full_string

# Example usage
full_string = "Hello, world!"
substring = "world"

if check_substring_in(full_string, substring):
  print(f"The substring '{substring}' is present in the string.")
else:
  print(f"The substring '{substring}' is not present in the string.")
