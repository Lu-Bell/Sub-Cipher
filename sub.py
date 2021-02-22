f = open("encrypt.txt", "w")

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

message = """
I chose the picture with the children jumping out of the building due to the house fire. This decision seemed like it was life or death type of decision. If I was in a building that was burning and my only chance of survival was jumping, I would take the leap. This ethical decision reminds of Kant’s categorical imperative because this a decision that you have to make. For example, if you are hungry you must eat in order to stop being hungry and for survival. If you want to make it out of the fire alive and your only option is to jump then you must jump. 
	Categorical imperative is the idea that you do what you have to do regardless of what other people may think of your decision. I believe all journalist should abide by this philosophy. If a journalist feels like he or she needs to publish a picture in order to notify every one of the events that took place they should do so. Seeing little children jumping from a building that’s on fire should not be kept secret. You must notify everyone in order to be prepared for future fires and show how urgent they should change their procedures for fires. The downfall of this idea is that everyone has a different idea of what they “need” or “must” do. If someone believes that they need to harm someone and it is okay to them in terms of their universal law then what can you say? I could tell them it’s wrong because in my universal laws that is wrong but if it isn’t to them then there’s really nothing I can do. 
	I believe if one were to look at this photo and not know the background story of it they’d probably think that both the kids survived especially because this photo was published and won an award. Usually photos of children do not involve death. I personally believe that the photographer is correct in publishing this photo because of the impact it had on Boston’s fire procedures. Yes, it is a sad and tragic event but it forced them to change their fire procedures. It made an impact on society by changing Boston’s fire procedure. If that picture was never posted people might not have ever known what kind of impact the fire and how poorly Boston handled the situation by allowing children to jump from a building in order to save their lives. 
	If I was the publisher and I needed to decide if I was going to post this picture then I would go with Kant’s categorical imperative, because according to my universal law it is something I must do to inform the people of how tragic the event was. The government does not always show the full scope or tragedy of certain events because sometimes it actually might be too tragic but it can also be for their own benefit. If I was a publisher and I had the power to show the world something of such importance I would do it one hundred percent.
	I can see why he did not post the impact of the jump. In my opinion, that is too much to publish because the photo of them jumping is enough. People already know that the young girl did not survive the fall, we do not need to see her remains after. That is painful and heartbreaking. Her family probably did not want that picture to be taken or published either. But, if the photographer felt the need to do so and it was his duty to take and post that picture he would have been correct in terms of the categorical imperative because no one else’s opinion matters if you feel like the action you must do needs be done.
""".lower()
encrypt = " "

for i in message:
    for key, value in dictionary.items():
        if i == key:
            encrypt += value

#print(encrypt, end = "")

#write the encrypted code to a file


f.write('Encrypted Message : {}\n'.format(encrypt))
f.close()

#decrypt

decrypt = " "
for i in encrypt:
    for key, value in dictionary.items():
        if i == value:
            decrypt += key

#print(decrypt, end = " ")