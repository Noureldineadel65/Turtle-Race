from turtle import Turtle, Screen
import random
TURTLE_SIZE = 20
game_ended = False
winner = ""
turtles = {
    "turtle1": {
        "color": "purple",
        "num": 1
    },
    "turtle2": {
        "color": "blue",
        "num": 2
    },
    "turtle3": {
        "color": "green",
        "num": 3
    },
    "turtle4": {
        "color": "pink",
        "num": 4
    },
    "turtle5": {
        "color": "orange",
        "num": 5
    },
    "turtle6": {
        "color": "red",
        "num": 6
    }
}


screen = Screen()

# Setting up the turtles
for key in turtles:
    turtles[key]["inst"] = Turtle()
    turtle_object = turtles[key]["inst"]
    turtle_object.shape("turtle")
    turtle_num = turtles[key]["num"]
    turtle_object.color(turtles[key]["color"])

    turtle_object.penup()
    turtle_object.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/4 - (50 * turtle_num) - TURTLE_SIZE/2)
    turtle_object.pendown()
answer = screen.textinput("Welcome to Turtle Race!", "Which color are betting on (purple/blue/green/pink/orange/red)?").lower()
while not game_ended:
    for key in turtles:
        turtles[key]["inst"].forward(random.randint(10,25))
        if int(turtles[key]["inst"].xcor()) >= -(TURTLE_SIZE - screen.window_width()/2):
            winner = turtles[key]["color"]
            game_ended = True
            break
if not answer == winner:
    print("You lost.")
else:
    print("You win!")
screen.exitonclick()
