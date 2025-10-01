def guessing():
import random 
random_int = random.radint(1,10)
guessing=int(input("Pick a number from 1-10"))
if guessing == random_int:
    print("Correct")

elif guessing > random_int:
    print("Your number is too high")
elif guessing < random_int:
    print("Your number is too low")