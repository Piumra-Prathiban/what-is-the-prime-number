def isPrimeNumber(num): #new function 
 current_number = 1  # Starting number
 divison_count = 0  # Starting number
 t = num
 while current_number <= t:  # Change the condition to run until current_number reaches x
    division_reminder = t % current_number # division by modulo operator
    if division_reminder == 0 :
     divison_count += 1
    current_number += 1
 if divison_count == 2 :
   return True #returns true if it is prime number
 return False #returns false if it is not a prime number


def nthPrimeNumber(n):  #making a function to call for prime number later on
    print("Function is running wait.... \n(Dont panick if it looks stuck)") #code running info

    current_number = 1  
    prime_number_counter = 0
    
    while prime_number_counter != n:

        if isPrimeNumber(current_number): # calling the function that we made on line 1
            prime_number_counter += 1

        current_number += 1
        
    return current_number - 1  # Return the last prime number found

# calling the function to print the answer
print(str(nthPrimeNumber(5)) + "  <---- Done") 
#                       ^^^^^^^ <--- change this number to find the prime number that you want