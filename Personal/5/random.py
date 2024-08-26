import random as r

start = 1
end = 10

rangeVal = r.randint(start,end)

for i in range(3):
    guess = input(f"Guess a Random Number between {start} and {end}: ")
    if guess == rangeVal:
        print("You guessed it!")
        break
    else:
        print("Wrong Guess. Try Again!")
        continue
