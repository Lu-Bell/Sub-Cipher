from collections import Counter

with open("encrypt.txt", "r") as e:
    words = e.read()
    x = Counter(words) #checks how often a letter appears in th encrypted file

print(x)
e.close()