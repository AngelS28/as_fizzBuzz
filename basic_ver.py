# Create the function
def fizzbuzz_basic():

    # Looping through numbers
    for i in range(1,101):
        # Checking for Multiples of 3 and 5 
        if 1 % 3 == 0 and i % 5 == 0:
        # If i is multiples of 3 and 5, output "FizzBuzz"
            print("FizzBuzz")
        # Checking for Multiples of 3 
        elif i % 3 == 0:
            print("Fizz")
        # If i is multiples of 3 output "Fizz"
        
        #Checking for Multiples of  5 
        elif i % 5 == 0:
            print("Buzz")
        # If i is multiples of 5 output "Buzz"
        else:
            print(i)
        # If i is neither of them, ouput i

# Main function call
if __name__ == "__main__":
    # Call the fizzbuzz function
    fizzbuzz_basic()