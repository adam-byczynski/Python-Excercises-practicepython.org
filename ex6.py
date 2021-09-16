#entered_string = input("Enter any set of words to check if it is a palindrome: ")

def reverse_loop(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word)-1-i]
    
    if x == word:
	    print('This is a Palindrome')
    else:
	    print('This is NOT a Palindrome')
    return


def is_palindrome(any_str):
    rev_str = any_str[::-1]
    rev_str1 = any_str[len(any_str):0:-1]
    rev_str2 = any_str[:-1]

    print("\n") #dla czytelnosci
    print("Entered string:  ",any_str)
    print("Reversed string: ", rev_str)
    print("\n") #dla czytelnosci

    if any_str == rev_str:
        print("Entered string is a palindrome!")
    else: 
        print("Entered string is not a palindrome!")
        print("\n") #dla czytelnosci
     
    print("Test 1: ",rev_str1)
    print("Test 2: ",rev_str2)
    return 





slowo = "kawiarka"
is_palindrome(slowo)
reverse_loop(slowo)

