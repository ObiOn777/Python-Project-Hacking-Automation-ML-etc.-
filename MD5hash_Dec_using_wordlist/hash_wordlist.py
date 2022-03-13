import hashlib
import tkinter as tk
from tkinter.filedialog import askopenfilename

root = tk.Tk()
root.withdraw()
filename = askopenfilename()
wordlist = filename

print('''
        ██████   ██████ ██████████   ██████████    █████                        █████         █████   █████  █████████                                            █████ ████   ███           █████   
        ░░██████ ██████ ░░███░░░░███ ░███░░░░░░█   ░░███                        ░░███         ░░███   ░░███  ███░░░░░███                                          ░░███ ░░███  ░░░           ░░███    
         ░███░█████░███  ░███   ░░███░███     ░     ░███████    ██████    █████  ░███████      ░███    ░███ ░███    ░░░     █████ ███ █████  ██████  ████████   ███████  ░███  ████   █████  ███████  
         ░███░░███ ░███  ░███    ░███░█████████     ░███░░███  ░░░░░███  ███░░   ░███░░███     ░███    ░███ ░░█████████    ░░███ ░███░░███  ███░░███░░███░░███ ███░░███  ░███ ░░███  ███░░  ░░░███░   
         ░███ ░░░  ░███  ░███    ░███░░░░░░░░███    ░███ ░███   ███████ ░░█████  ░███ ░███     ░░███   ███   ░░░░░░░░███    ░███ ░███ ░███ ░███ ░███ ░███ ░░░ ░███ ░███  ░███  ░███ ░░█████   ░███    
         ░███      ░███  ░███    ███  ███   ░███    ░███ ░███  ███░░███  ░░░░███ ░███ ░███      ░░░█████░    ███    ░███    ░░███████████  ░███ ░███ ░███     ░███ ░███  ░███  ░███  ░░░░███  ░███ ███
        █████     █████ ██████████  ░░████████     ████ █████░░████████ ██████  ████ █████       ░░███     ░░█████████      ░░████░████   ░░██████  █████    ░░████████ █████ █████ ██████   ░░█████ 
        ░░░░░     ░░░░░ ░░░░░░░░░░    ░░░░░░░░     ░░░░ ░░░░░  ░░░░░░░░ ░░░░░░  ░░░░ ░░░░░         ░░░       ░░░░░░░░░        ░░░░ ░░░░     ░░░░░░  ░░░░░      ░░░░░░░░ ░░░░░ ░░░░░ ░░░░░░     ░░░░░  
                                                                                                                                                                                              
                                                                                                                                                                                              
                                                                                                                                                                                              
         █████                         █████  █████     █████    █████       ███      █████               ███       █████████                                                          ███            
        ░░███                         ░░███  ░░███     ░░███    ░░███       ░░░      ░░███               ░░░       ███░░░░░███                                                        ░░░             
         ░███████  █████ ████          ░███  ███████   ███████   ░███████   ████   ███████   ██████      █████    ░███    ░███  ████████   ██████   █████████████    █████  ████████  ████            
         ░███░░███░░███ ░███           ░███ ░░░███░   ░░░███░    ░███░░███ ░░███  ███░░███  ███░░███    ░░███     ░███████████ ░░███░░███ ░░░░░███ ░░███░░███░░███  ███░░  ░░███░░███░░███            
         ░███ ░███ ░███ ░███           ░███   ░███      ░███     ░███ ░███  ░███ ░███ ░███ ░███████      ░███     ░███░░░░░███  ░███ ░░░   ███████  ░███ ░███ ░███ ░░█████  ░███ ░░░  ░███            
         ░███ ░███ ░███ ░███           ░███   ░███ ███  ░███ ███ ░███ ░███  ░███ ░███ ░███ ░███░░░       ░███     ░███    ░███  ░███      ███░░███  ░███ ░███ ░███  ░░░░███ ░███      ░███            
         ████████  ░░███████           █████  ░░█████   ░░█████  ████ █████ █████░░████████░░██████      ░███     █████   █████ █████    ░░████████ █████░███ █████ ██████  █████     █████           
        ░░░░░░░░    ░░░░░███          ░░░░░    ░░░░░     ░░░░░  ░░░░ ░░░░░ ░░░░░  ░░░░░░░░  ░░░░░░       ░███    ░░░░░   ░░░░░ ░░░░░      ░░░░░░░░ ░░░░░ ░░░ ░░░░░ ░░░░░░  ░░░░░     ░░░░░            
                    ███ ░███                                                                         ███ ░███                                                                                         
                   ░░██████                                                                         ░░██████                                                                                          
                    ░░░░░░                                                                           ░░░░░░                                                                                                                                                                         
''')

hash = input("Enter Hashed password Here: ")

pass_found = 0
try:
    pass_file = open(wordlist, "r")
except:
    print("Error")
    print(wordlist, "is not found.\nPlease select path file again")
    quit()

for word in pass_file:
    enc_word = word.encode("utf-8")
    hash_word = hashlib.md5(enc_word.strip())
    digest = hash_word.hexdigest()
    if digest == hash:
        print(f"Password Found.\nThe Password is: {word}")
        pass_found = 1
        break

if pass_found != 1:
    print("Password is not found in the", wordlist, "file")
    print("\n")
print("Good bye")
