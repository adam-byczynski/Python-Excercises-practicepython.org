
while True:
    number1 = int(input("Enter one number: "))
    number2 = int(input("to check if it divides evenly into: "))
    if number2 > number1: 
        print("Second number can't be larger than the first!\nTry again.\n")
        continue  
    if number1 % number2 == 0:
        print("\n" + str(number1) + " divides evenly into " + str(number2) + ".")
    else:
        print("\n" + str(number1) + " doesn't divide evenly into " + str(number2) + ".")
    break

input("\nPress Enter to terminate the program...")