f = open("encrypt.txt", "w", encoding = "utf8") #file for encryption with no key
a = open("Alice.txt", "w", encoding = "utf8") #file for encryption with key given a password
c = open("corpus.txt", "r+", encoding = "utf8")

# Dictionary for the substitution key
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

encrypt = " "
#---- ALICE'S VIEW ----
corpus = c.read().lower()
#encryption method
def encryption(m):
    global encrypt
    for i in m:
        for key, value in dictionary.items():
            if i == key:
                encrypt += value
    return encrypt

#method that asks for password to access the key
def get_key():
    passcode = input("Enter password for key and encrypted message: ")
    if passcode == password:
        print("Encrypted message has been sent to Alice.txt")
        return str((dictionary))

#writes the encrypted code to a file
f.write('Encrypted Message : {}\n'.format(encryption(corpus)))
f.close()

a.write('Encrypted Message : {}\n'.format(encryption(corpus)))
a.write("Key: {}".format(get_key()))
c.close()
#writes alices code with password to the file
a.close()

#-----BOB'S VIEW-----

#decryption function
d = open("decrypt.txt", "w") #file for decryption
decrypt = " "
def decryption():
    global decrypt
    for i in encrypt:
        for key, value in dictionary.items():
            if i == value:
                decrypt += key
    return decrypt

#print(decrypt, end = " ")
d.write('Encrypted Message : {}\n'.format(encryption(corpus)))#writes the encrypted code
d.write('\nDecrypted Message : {}\n'.format(decryption()))#writes the decrypted code
d.close()


