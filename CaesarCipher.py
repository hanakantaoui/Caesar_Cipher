print("\033[34m"+"------------------||WELCOME TO CAESAR CIPHER||---------------------"+"\033[0m")

def caesar_cipher(text,key,mode):
    result=""
    if mode=="encrypt":
        key=key
    else:
        key=(-key)

    for char in text:
        if char.isalpha():
            if char.isupper():
               start=ord("A")
            else:
                start=ord("a")
            result+=chr((ord(char)-start+key)%26+start)
        else:
            result+=char
    return result

#print("Encryption of HELLO :  ", caesar_cipher("HELLO",3,"encrypt"))    
#print("Decryption of khoor : ",caesar_cipher("khoor",3,"decrypt")) 
#print("Encryption of hello : ",caesar_cipher("hello",-3,"encrypt"))             

text=input("\033[35m"+"Enter you text to encrypt or decrypt : "+"\033[0m")
key=int(input("\033[35m"+"Please, enter your key : "+"\033[0m"))
mode=input("\033[35m"+"Enter your mode : "+"\033[0m")
print("\033[36m"+"Caesar Cipher --> "+"\033[0m",caesar_cipher(text,key,mode))           


    