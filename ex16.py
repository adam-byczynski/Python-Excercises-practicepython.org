# Ex16
# Password generator

import time
from msvcrt import getch
import random
import os
import getpass

def initial_setup():
    os.system('cls')
    print("Welcome to password generator!")
    
def generate_pass(l, d):  #length, difficult
    choose_d={
        '1': "0123456789",
        '2': "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        '3': "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?0123456789"
    }
    print("Press Enter to generate another password, S to save it to the text document, or Escape to quit:")
    while(True):
        #usr_path = os.path.expanduser()
        temp_1= choose_d.get(d)
        g_pass = "".join(random.sample(temp_1, k=int(l)))
        print("Is this password ok?", g_pass)
        dec = ord(getch())
        if dec == 27:
            quit()
        elif dec == 13:
            continue
        elif dec == 115:
            username = getpass.getuser()
            path = open(f'C:\\Users\\{username}\\Desktop\\generated_password.txt','w')
            path.write("Generated password: " + g_pass)
            path.close()
            print("Password saved to Desktop!")
            time.sleep(3)
            break
    
    
def main():
    while True:
        initial_setup()
        leng = input("How long do you want your password to be: ")
        if ord(getch()) == 27: quit()
        print("1-numbers, 2-letters, 3-all char")
        diff = input("How difficult should it be: ")
        if ord(getch()) == 27: quit()
        generate_pass(leng,diff)
        
main()
