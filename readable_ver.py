# Call the function
def fizzbuzz_readable():
    # Looping through numbers 1 to 100
    for i in range(1,101):
        # Initialize an empty string to store the output 
        output = ""
        # Check if the number is divisible by 3
        if i % 3 == 0:
            # Append "Fizz" to the output
            output += "Fizz"
        # Check if number is divisible by 5
        if i % 5 == 0:
            # Append "Buzz" to the output
            output += "Buzz"
            
        # Check if the output is still empty (not divisible by 3 or 5)
        if not output:
            # If output is empty, assign the number itself to ouput
            output = i
        # Print output 
        print(output)

# Main function call
if __name__ == "__main__":
    # Call the fizzbuzz function
    fizzbuzz_readable()
