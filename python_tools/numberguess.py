import random

# Step 1: Generate a random number between 1 and 20
number = random.randint(1, 20)

print("I'm thinking of a number between 1 and 20.")

# Step 2: Loop for guesses
for attempt in range(1, 6):
    guess = int(input(f"Attempt {attempt}: Enter your guess:"))

    if guess == number:
        print("Correct! You've guessed the number!")
        break
    elif guess < number:
        print ("Too low!")
    else:
        print("Too high!")

# Step 3: If not guessed, reveal the number
else:
    print(f"Sorry, you're out of guesses. The number was {number}.")

