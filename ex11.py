 
 
 
 
def get_integer():
    return int(input("Give me a number: "))

def is_prime(number):
    for x in range(1,number):
        if number % x !=0 and number % 1==0:
            return TRUE
        
        
a = get_integer()
print("A=",a)
is_prime(a)