# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer loop using while to handle rows
while row < size:
    # Inner loop using for to print asterisks on the same line
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Print newline after each row
    row += 1

