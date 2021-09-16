from random import *

list_length = randint(10,20)
my_list = []

while len(my_list) < list_length:
  my_list.append(randint(1, 100))

my_list.sort()

print("\nList Length = " + str(list_length))
print(my_list)

max_num = randint(20,40)
#int(input("\nPlease enter the maximum number from the list: "))

print("Desired max number: " + str(max_num))

combined_list = []

for i in range(len(my_list)):
    if my_list[i-1] <= max_num:
        combined_list.append(my_list[i-1]) 

print(combined_list)
input("Press Enter to continue...")
