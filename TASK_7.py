import random
number = random.randint(1, 100)
nguesses = 0
print("Guess the number between 1 to 100")
while True:
    guess = int(input("Guess the number : "))
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("Congratulations")
        print("You guessed it in ",nguesses," attempts")
        break
    nguesses += 1
