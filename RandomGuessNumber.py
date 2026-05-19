import random 

secret_number = random.randint(1,100)

attemps = 0

while True:
    guess = int(input("Enter the number: "))

    attemps += 1

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct! You have guessed the number. ")
        print("Attemps:", attemps)
        break
