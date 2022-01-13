import random
print("number guessing game")

number= random.randint(1,9)
chances= 0

while chances<5:
    guess= int(input("enter your guess"))
    if guess== number:
        print("u win GG")
        break
    elif guess<number:
        print("your guess is too low")
    else:
        print("your guess is too high")
    chances+=1
if not chances<5:
    print("u lose L")