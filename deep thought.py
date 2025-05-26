
question = input("what is the answer to the great question of life , the universe and everything? ")

if question .strip()== "42":

    print("yes")

elif question.lower().strip() == "forty-two":
    print ("yes")

elif question.lower().strip() == "forty two":
    print("yes")       

else :
    print("no")

