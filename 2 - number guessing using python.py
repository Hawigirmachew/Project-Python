import random
attempt = 10
guess= None
num = random.randint(1,11)
print(num)
for i in range(attempt):
    print("Enter a number between 1 and 10 ")
    guess = input()
    guess = int(guess)
    if guess == num:
        print("You win!")
        break
    else:
        if guess > num:
            print(str(guess) + " is larger")
        else:
            print(str(guess) + " is smaller")
        print("Try again!")
        attempt-=1
        continue
