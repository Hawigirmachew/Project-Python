import random

flag = True 

while flag:
    num = print("Enter an Upper bound: ")
    if num.isdigit():
        print("Ready to play")
        num = int(num)
        flag = False
    else:
        print("Try to enter a number above zero")
        
    
    
secret_number = random.randint(0,100)

guess = None
while guess != secret_number:
    print("Enter a number between 0 and 100")
    guess = int(input())
    if guess == secret_number:
        print("Conguratulation")
        break
    else:
        print("Please try again")
