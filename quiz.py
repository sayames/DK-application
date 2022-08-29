print("Welcome to my quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Great, let's get started!")
score = 0

answer = input("in what year did neil armstrong land on the moon? ")
if answer.lower() == "1969":
    print ("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What is the biggest city in the UK? ")
if answer.lower() == "london":
    print ("Well done!")
    score += 1
else: 
    print("Unfortunately, that is incorrect!")

answer = input("What does GPU stand for ")
if answer.lower() == "graphics processing unit":
    print ("That's right!")
    score += 1
else: 
    print("Better luck next time!")

answer = input("What is the capital of Canada? ")
if answer.lower() == "ottawa":
    print ("Yes, correct!")
    score += 1
else: 
    print("No, the correct answer is ottawa!")

print("You scored " + str(score) + " out of 4!")
print("That's " + str((score/4) * 100) + " %!") 