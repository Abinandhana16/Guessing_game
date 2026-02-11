import random
secret_number = random.randint(1, 100)
attempts = 0
guess = None
print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1
    difference = abs(secret_number - guess)

    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        print("Total attempts:", attempts)

    elif difference <= 5:
        if guess < secret_number:
            print("Very close! Just a little higher.")
        else:
            print("Very close! Just a little lower.")

    elif guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")
