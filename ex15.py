# Ex15
# Write a function that asks the user for a string containing multiple words. Print
# back to the user the same string, except with the words in backwards order. 


usr_str = input("Input string containing multiple words: ")

temp_list = ' '.join(usr_str.split()[::-1])

print(temp_list)

