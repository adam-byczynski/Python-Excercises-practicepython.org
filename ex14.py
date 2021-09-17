# Ex14
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

def no_dup(input_list):
    for elem in input_list:
        if elem not in temp_list:
            temp_list.append(elem)
    print(*temp_list)

a = [1, 1, 2, 3, 5, 5, 8, 13, 21, 21, 34, 55, 89]
temp_list = []
print(*set(a))
no_dup(a)