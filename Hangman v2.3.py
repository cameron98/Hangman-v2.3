"""
Hangman v2.3

New update streamlining of code using classes


Create a GUI hangman game for STEM day/school
Begin with window to type in word, hidden with *.
Must display list of letters, hangman screen and _ for letters.

Created by Cameron
cameron.finnie@yahoo.co.uk
"""
import tkinter as tk
import turtle
from sys import exit

class Buttons:
    
    def __init__(self, letter, column, row):
        self.letter = letter
        self.column = column
        self.row = row

    def create(self):
        self.tkbutton = tk.Button(window, text=self.letter, bg = colour, font=FONT,
                         command=lambda : check(self.letter))
        self.tkbutton.place(relx=self.column, rely=self.row)


def EXIT():
    window.destroy()
    exit()

def restart():
    global missing
    t.reset()
    for letter in missing:
        eval(letter).create()
    missing = []                   
    window.wm_state('iconic')
    Word()


#function to check if guess is in word
def check(guess):
    global wordList, correct, attempt, missing
    occurences = word.count(guess)
    if occurences > 0:
        while occurences > 0:
            location = word.index(guess)
            word[location] = "!"
            wordList[location] = guess
            occurences -= 1
            correct += 1
        wordDisplay.config(text=wordList)
        if correct == total:
            wordList = ("Correct! The word was " + final)
            wordDisplay.config(text=wordList)
    else:
        attempt += 1
        draw(attempt)
    guesses = []
    missing.append(guess)
    guesses.append(guess)
    guess = eval(guess) #changes string into variable
    guess.tkbutton.place_forget()
    
    #attatch new function to this to trigger drawing
    
def draw(step):
    if step ==1:
        t.penup()
        t.goto(-300, -200)
        t.pendown()
        t.forward(600)
        t.penup()
        t.goto(-100,-200)
    elif step ==2:
        t.left(90)
        t.pendown()
        t.forward(400)
    elif step ==3:
        t.right(90)
        t.forward(250)
    elif step ==4:
        t.penup()
        t.goto(-100, 160)
        t.left(45)
        t.pendown()
        t.forward(56.56854249)
    elif step ==5:
        t.penup()
        t.goto(150,200)
        t.setheading(270)
        t.pendown()
        t.forward(40)
    elif step ==6:
        t.speed(0)
        t.seth(180)
        t.circle(17)
    elif step == 7:
        t.speed(5)
        t.penup()
        t.goto(150,125)
        t.pendown()
        t.seth(270)
        t.forward(80)
    elif step ==8:
        t.penup()
        t.goto(120, 100)
        t.seth(0)
        t.pendown()
        t.forward(60)
    elif step ==9:
        t.penup()
        t.goto(150,45)
        t.right(45)
        t.pendown()
        t.forward(45)
    elif step ==10:
        t.penup()
        t.goto(150, 45)
        t.right(90)
        t.pendown()
        t.forward(45)
        wordDisplay.config(text="OUT OF LIVES! The word was " + final)
        



def START():
    #note insert refresh options for window in START to allow replayable program
    global word, wordDisplay, wordList, total, correct, attempt, final
    word = box.get()
    final = word
    final.upper()
    word = word.upper()
    word = list(word)
    wordList = []
    entry.destroy()
    for n in range(len(word)):
        wordList.append("_")
    ', '.join(wordList)
    wordDisplay.config(text=wordList)
    total = len(word)
    correct = 0
    t.penup()
    t.goto(-300,-200)
    attempt = 0
    window.deiconify()
        
    
#function for button that takes word to enter
def Word():
    global box, entry, reference
    guesses = []
    reference = []
    entry = tk.Toplevel()
    label = tk.Label(entry, text="Enter word:")
    label.pack()
    box = tk.Entry(entry, show="*")
    box.pack()
    enter = tk.Button(entry, text="START", command=START)
    enter.pack()
    entry.mainloop

missing = []
    
colour = "#538bad"
FONT = ("Arial", 20)
row1 = 0.3
row2 = 0.4
row3 = 0.5
row4 = 0.6
row5 = 0.7
row6 = 0.8
column1 = 0.05
column2 = 0.1
column3 = 0.15
column4 = 0.2
column5 = 0.25



#code to find monitor resolutions
res = tk.Tk()
Sheight = res.winfo_screenheight()
Swidth = res.winfo_screenwidth()
res.destroy()
res.mainloop()





window = tk.Tk()
window.title("Hangman")
window.attributes('-fullscreen', 'True')
#To add a background colour 
window.configure(background=colour)
#To set the window icon window.wm_iconbitmap('icon.ico')

#To add a background colour bg= for forgeground fg=
title = tk.Label(window, text="HANGMAN", bg=colour, font=("Arial", 50))
title.place(relx=0.38, rely=0.05)

#creation of exit button
EXIT = tk.Button(window, text="EXIT", bg=colour, command=EXIT)
EXIT.place(relx=0.5, rely=0.95)


A = Buttons('A', column1, row1)
A.create()
B = Buttons('B', column2, row1)
B.create()
C = Buttons('C', column3, row1)
C.create()
D = Buttons('D', column4, row1)
D.create()
E = Buttons('E', column5, row1)
E.create()
F = Buttons('F', column1, row2)
F.create()
G = Buttons('G', column2, row2)
G.create()
H = Buttons('H', column3, row2)
H.create()
I = Buttons('I', column4, row2)
I.create()
J = Buttons('J', column5, row2)
J.create()
K = Buttons('K', column1, row3)
K.create()
L = Buttons('L', column2, row3)
L.create()
M = Buttons('M', column3, row3)
M.create()
N = Buttons('N', column4, row3)
N.create()
O = Buttons('O', column5, row3)
O.create()
P = Buttons('P', column1, row4)
P.create()
Q = Buttons('Q', column2, row4)
Q.create()
R = Buttons('R', column3, row4)
R.create()
S = Buttons('R', column4, row4)
S.create()
T = Buttons('T', column5, row4)
T.create()
U = Buttons('U', column1, row5)
U.create()
V = Buttons('V', column2, row5)
V.create()
W = Buttons('W', column3, row5)
W.create()
X = Buttons('X', column4, row5)
X.create()
Y = Buttons('Y', column5, row5)
Y.create()
Z = Buttons('Z', column3, row6)
Z.create()



canvas = tk.Canvas(window, height=Sheight*0.6, width=Swidth*0.6)
canvas.place(relx=0.35, rely=row1)

t = turtle.RawTurtle(canvas)
screen = t.getscreen()
screen.bgcolor=("white")

wordDisplay = tk.Label(window, text="WORD", font=("Arial",30), bg=colour)
wordDisplay.place(relx=0.1, rely=0.2)

RESTART = tk.Button(bg=colour, text="RESTART", command=restart)
RESTART.place(relx=0.7, rely=0.95)

Word()

window.mainloop()
