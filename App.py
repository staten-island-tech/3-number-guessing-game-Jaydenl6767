win = 0
import random 
random_int = random.randint(1,10)
print(f"Random integer: {random_int}")

while win == 0:
    guessing=(int(input("Pick a number from 1-10 ")))
    if guessing == random_int:
        print("Correct")
        win=1
        print(f"you guessed{guess_history}")

    elif guessing > random_int:
        print("Your number is too high")
        guess_history.append(guess)

    elif guessing < random_int:
        print("Your number is too low")
        guess_history.append(guess)

