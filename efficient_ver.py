def fizzbuzz_efficient(n):
# Declare a list of strings to store the results
    result = []

# Loop from 1 to n (inclusive)
    for i in range(1, n+1):
        # Check if i is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
            # Add "Fizzbuzz" to result list

        # Check if i is divisible by 5
        elif i % 5 == 0:
            result.append("Buzz")
            # Add "Buzz" to reuslt list

        # Check if i is divisible by 3
        elif i % 3 == 0:
            result.append("Fizz")
        # Add "Fizz" to result list

        else:
            result.append(str(i))
            # Add the current nuber as a string to the result list

    return result

# Set number to get for n 
n = 100

# Call the fizzbuzz function to get the result
result = fizzbuzz_efficient(n)

# Print result 
print (' '.join(result))