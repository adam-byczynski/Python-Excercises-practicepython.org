from random import *

divided_num = randint(1,30)
#int(input("Please enter an any number: "))

print("\nEntered number: " + str(divided_num))

all_numbers = list(range(1,divided_num+1))
divisors_list = []

for i in range(len(all_numbers)):
    if divided_num % all_numbers[i] == 0:
        divisors_list.append(all_numbers[i])

print("List of divisors:",end=" ")
print(divisors_list)

#input("Press Enter to terminate the program...")
