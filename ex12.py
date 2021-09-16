# Ex12 
# Out of list of numbers write out only first and ladt number

import random

def first_last():
    generated_list = sorted(random.sample(range(1,30), random.randint(10,20)))
    print(*generated_list, sep = " ")
    new_list = []
    new_list.append(generated_list[0])
    new_list.append(generated_list[-1])
    print(*new_list, sep = " ")
    
first_last()
    
#shorter, different version 
    
def short():
    generated_list = sorted(random.sample(range(1,30), random.randint(10,20)))
    print(*generated_list, sep = " ")
    print(generated_list[0],generated_list[-1])
    
short()