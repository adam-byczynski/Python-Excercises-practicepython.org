#This program checks whether given number is prime or not
 
def get_integer():
    return int(input("\nGive me a number: "))

def is_prime(number):
    prime_status = True
    divisors = []
    for x in range(1,number):
        if number % x == 0 and x != 1:
            prime_status = False
            divisors.append(x)
    if prime_status == True: print("It's prime!!!"); print("It divides only by: 1 and",x+1)
    else: 
        print("It's not a prime..."); 
        divisors.append(x+1)
        print("It divides by:",*divisors, end=" ")

#jak to poprawic zeby zawierało też siebie  
given_number = get_integer()
print("Given number =",given_number)
is_prime(given_number)