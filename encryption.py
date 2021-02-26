dictionary = {
    "a" : "z",
    "b" : "x",
    "c" : "d",
    "d" : "g",
    "e" : "p",
    "f" : "t",
    "g" : "q",
    "h" : "l",
    "i" : "y",
    "j" : "a",
    "k" : "b",
    "l" : "c",
    "m" : "i",
    "n" : "m",
    "o" : "n",
    "p" : "w",
    "q" : "r",
    "r" : "v",
    "s" : "o",
    "t" : "k",
    "u" : "e",
    "v" : "u", 
    "w" : "h",
    "x" : "s",
    "y" : "f",
    "z" : "j", 
    " " : " "
}

password = "1234" #password for key
decrypt = " "
encrypt = " "

def get_key():
    global decrypt
    passcode = input("Enter password for key and encrypted message: ")
    if passcode == password:
        for i in encrypt:
            for key, value in dictionary.items():
                if i == value:
                    decrypt += key
        for i, j in dictionary.items():
            print(i, "=", j)
    return "Decrypted Message: "+decrypt

#---- ALICE'S VIEW ----

m = input("Enter a string you would like to be encrypted: ")
encrypt = " "
#encryption method
for i in m:
    for key, value in dictionary.items():
        if i == key:
            encrypt += value
print("\nEncrypted Message: "+encrypt)
#method that asks for password to access the key

#------BOB'S VIEW-------
choice = input("\nWould you like to decrypt this message? ")

if choice == "yes".lower():
    print(get_key())
if choice == "no".lower():
    print("Ok.")

        