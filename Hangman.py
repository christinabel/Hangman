import random,turtle

with open("hangman_words.txt",'r') as f:
    words = random.choice(f.readlines()).strip()

allowed_guesses = 8 
guess = ''
done = False

screen = turtle.Screen()
screen.bgcolor("lightblue")


t = turtle.Turtle()
t.speed(0)
t.pensize(4)
t.hideturtle()

def draw_words(word):
    t.penup()
    t.setposition(-150,-150)
    for letter in word:
        if letter != ' ':
            t.setheading(0)
            t.write(letter, font = ("Adobe Arabic",20,"normal"))
        t.forward(42)
        
def draw_lines(length):
    t.penup()
    t.setposition(-155, -150) 
    t.pendown()
    for _ in range(length):
        t.setheading(0)
        t.forward(30) 
        t.penup()
        t.forward(10)
        t.pendown()

def draw_hangman(x):
    if x == 7:
        t.penup()
        t.setposition(-120,-15)
        t.right(-90)
        t.pendown()
        t.forward(250)
        t.right(90)
        t.forward(150)
    elif x == 6:
        t.right(90)
        t.forward(50)
        t.right(90)
        t.circle(25)
    elif x == 5:
        t.penup()
        t.setposition(30,135)
        t.right(-90)
        t.pendown()
        t.forward(90)
    elif x == 4:
        t.penup()
        t.setposition(30,110)
        t.right(45)
        t.pendown()
        t.forward(30)
    elif x == 3:
        t.penup()
        t.setposition(30,110)
        t.right(-90)
        t.pendown()
        t.forward(30)
    elif x == 2:
        t.penup()
        t.setposition(30,45)
        t.right(90)
        t.pendown()
        t.forward(30)
    elif x == 1:
        t.penup()
        t.setposition(30,45)
        t.right(-90)
        t.pendown()
        t.forward(30)
        pass
    
while allowed_guesses > 0:
    for letter in words:
        if letter.lower() in guess:
            print(letter, end='')
        else:
            print('_', end =' ')

    
    guesses = input(f'\nAllowed guess: {allowed_guesses}\n''Enter your guess:')
    guess += guesses.lower()
    if guesses not in words:
            allowed_guesses -=1
            draw_hangman(allowed_guesses)
    if allowed_guesses == 0:
            break
    if all(letter.lower() in guess for letter in words):
        done = True
    
draw_words(words.lower())
draw_lines(len(words.lower()))

if done:
    t.penup()
    t.setposition(-155,-120)
    t.write("You won", font=('Adobe Arabic',20,'normal'))
else:
    t.penup()
    t.setposition(-155,-120)
    t.write("You lose", font=('Adobe Arabic',20,'normal'))
turtle.done()               
            
        
