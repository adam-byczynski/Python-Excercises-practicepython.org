# Ex13
# Get the number, then generate that many numbers from Fibonacci sequence

def get_number():
    number = int(input("\nHow many Fibonacci elements print? "))
    return number

def generate_Fib():

    fib = [1,1]
    for i in range(2,get_number()):
       fib.append(fib[i-1]+fib[i-2])
    
    print(*fib,sep=" ")
    print("\n")
    
generate_Fib()