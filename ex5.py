from random import *

def generate_list(list_size):
      blank_list = []
      while len(blank_list) <= list_size:
            blank_list.append(randint(1,30))
      blank_list.sort()
      return blank_list

list_one_size = randint(10,20)
list_two_size = randint(10,20)
list_one = generate_list(list_one_size)
list_two = generate_list(list_two_size)
list_common = []

for i in list_one:
      for j in list_two:
            if j == i:
                  list_common.append(j)

list_common.sort()
print("\nList one: ",list_one)
print("List two:",list_two)
print("\nList of common numbers: ",set(list_common),"\n")

#test = list(set(a).intersection(set(b))) ?????

#input("Press Enter to terminate the program...")

