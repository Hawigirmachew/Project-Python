from tkinter import Tk, ttk
from tkinter import * 
import random


root = Tk()
root.title("Python game")
root.geometry("400x400")
root['bg']='yellow'

secret =random.randint(1,10)
number = IntVar()
display= StringVar()
attempt = 5

def compare_and_check():
    global attempt

    user_input = number.get()

    if attempt > 0:
        if secret == user_input :
            msg= "You won!"
        elif secret >user_input :
            attempt-= 1
            msg = "Number is lesser than the secret number"
        elif secret < user_input :
            attempt -=1
            msg = "Number is greater than the secret number"
        else:
            msg="Something went wrong"
    else:
        msg="Sorry you  lost the game"
    display.set(msg)    





#title 
Label(
    root,
    text="Number Guessing Game",
    font="Times 20",
    fg="brown",
    relief="raised"
).pack(pady=10)
  
Entry(
    root,
    textvariable= number,
    font=("san sarif",20)
).pack(pady=(40,20)) 
Button(
    root,
    text="Sumbit Guess",
    font=("Times 20"),
    command= compare_and_check
).pack(pady=(60,20))

Label(
    root,
    font=("helvetica 16"),
    textvariable= display
).pack(pady=(10,5))
















#main loop   
root.mainloop()
