# Classic FizzBuzz algorithm
# Print all numbers from 1 to 100, instead of multiples of 3 print "Fizz", for multiples of 5 print "Buzz" and for multiples of 3 and 5 print "FizzBuzz"

for num in range(1, 101): #Use range function to provide the numbers from 1 to 100
    if num % 5 == 0 and num % 3 == 0:  #Use if and modulus to print the respective strings in place of numbers 
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    

# Result print "Fizz", "Buzz" and "FizzBuzz" as expected