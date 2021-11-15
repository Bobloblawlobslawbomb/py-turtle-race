from turtle import Turtle, Screen
from random import randint

TURTLE_RAINBOW = ["red", "orange", "yellow3", "green", "blue", "purple"]
X_COR = -235

screen = Screen()
timmy = Turtle(shape="turtle")
screen.setup(width=500, height=400)

racing = False

user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: "
)

y_cor = -125
turtle_list = []

for shade in TURTLE_RAINBOW:
    name = shade
    name = Turtle(shape="turtle")
    name.color(shade)
    name.penup()
    starting_pos = (X_COR, y_cor)
    name.goto(starting_pos)
    y_cor += 50
    turtle_list.append(name)

if user_bet:
    racing = True

timmy.hideturtle()

while racing:
    for hero in turtle_list:
        distance = randint(0, 10)
        hero.forward(distance)
        if hero.xcor() > 230:
            racing = False
            winner = hero.pencolor()
            if winner == "yellow3":
                winner = "yellow"
            if winner == user_bet.lower():
                print(
                    f"You've Won!!! The winner is: {winner.upper()} and your bet was: {user_bet.upper()}.")
            else:
                print(
                    f"You've Lost. The winner is: {winner.upper()} and your bet was: {user_bet.upper()}.")
