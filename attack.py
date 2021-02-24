from collections import Counter
f = open("Eve.txt", "w")
with open("encrypt.txt", "r") as e:
    words = e.read()
    x = Counter(words) #checks how often a letter appears in the encrypted file
    count = 0

sort_orders = sorted(x.items(), key=lambda y: y[1], reverse=True)
count = sum(x.values())
for i in sort_orders:
	#print(i[0], ":", i[1])
    percent = ((i[1] / count) * 100)
    print(i[0], ":", percent)

#print(count)



e.close()
f.close()
#e - .12
#t - .9
#a - .8

