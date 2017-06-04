from random import randint

random = (randint(1,10))
# print random


while True:
    raw = int(raw_input("Guess the number: "))

    if raw != random:
        print "Try again"

    if raw == random:
        print "You've guessed the number correctly! What a Genius!!"
        break
