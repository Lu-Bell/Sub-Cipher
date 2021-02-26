from collections import Counter
print("YOUR ENCRYPTION SCHEME IS BEING COMPROMISED!")
print("\nLETTER FREQUENCY: \n")
boolean = True
q = 1

with open("encrypt.txt", "r+") as e:
    words = e.read().lower()
    x = Counter(words) #checks how often a letter appears in the encrypted file
    count = 0

sort_orders = sorted(x.items(), key=lambda y: y[1], reverse=True)
count = sum(x.values())
for i in sort_orders:
	#print(i[0], ":", i[1])
    percent = ((i[1] / count) * 100)
    print(i[0], ":", "{:.2f}".format(percent))

#print(count)


e.close()

#e - .12
#t - .9
#a - .8

