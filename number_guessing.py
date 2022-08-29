import random 
# imports the built-in random module

print("Welcome to the number guessing game. The computer will choose a number and you will have to guess it.")

user_number = input("Please set a maximum number: ")

if user_number.isdigit(): 
# if true 

    user_number = int(user_number)

    if user_number <= 0:
        print("Your number has to be larger than 0!")
        quit()
else: 
    print("Please type a digit next time.")
    quit()

random_number = random.randint(0, user_number) 
# 11 isn't included with randrange, but is is with randint. If no start value is included, randrange starts number will be = 0

guesses = 0

while True: 
    guesses += 1
    user_guess = input("Now, make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a digit instead.")
        continue

    if user_guess == random_number:
        print("You guessed right!")
        break
    elif user_guess > random_number: 
    # elif cleans it up
            print("The number is smaller!")
    else:
            print("The number is bigger!")

print("You got it in", guesses, "guesses")