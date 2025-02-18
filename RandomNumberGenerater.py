import random, time

number = random.randint(1, 10)
if input("Guess the number!") == number:
    print("congrats you guessed the correct number")
else:
    print("incorrect guess, correct number was", number)

time.wait(5)
exit()
