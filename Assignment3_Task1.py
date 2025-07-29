# Function to calculate factorial using a loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Take input from user
num = int(input("Enter a number: "))

# Call the function and print the result
print(f"Factorial of {num} is: {factorial(num)}")
