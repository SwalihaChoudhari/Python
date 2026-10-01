import random
target=random.randint(1,100)

while True:
    number=(input("Guess the number or quit: "))
    if number=="quit":
        break
    number=int(number)
    if number==target:
        print("You guessed the right number!")
        break
    elif number<target:
        print("your number was too small,take a bigger guess!")
    else:
        print("your number is too big,take a smaller guess!")
        
    