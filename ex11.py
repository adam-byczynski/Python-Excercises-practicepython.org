#This program checks whether given number is prime or not
 
import math 
 
def get_integer():
    return int(input("\nGive me a number: "))

def is_prime(number):
    prime_status = True
    divisors = []
    for x in range(1,math.ceil(number/2)):
        if number % x == 0 and x != 1:
            prime_status = False
            if x not in divisors: divisors.append(x)
            if number/x not in divisors: divisors.append(int(number/x))
    if prime_status == True: 
        print("It's prime!!!") 
        print("It divides only by: 1 and", 2 * x if x % 2 == 0 else 2*x+1)
    else: 
        print("It's not a prime..."); 
        divisors.append(2*x if x % 2 == 0 else 2*x+1) 
        divisors.sort()
        print("It divides by:",*divisors, end=" ")

given_number = get_integer()
is_prime(given_number)