import math

# Ask the user for a number
num = float(input("Enter a number: "))

# Perform calculations
sqrt_val = math.sqrt(num)
log_val = math.log(num)
sine_val = math.sin(num)

# Display the results with matching labels
print(f"\nSquare root: {sqrt_val}")
print(f"Logarithm: {log_val}")
print(f"Sine: {sine_val}")
