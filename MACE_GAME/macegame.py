import turtle

space=turtle.Screen()

space.bgpic("background.gif")
space.addshape("spaceman.gif")
spaceman=turtle. Turtle()
spaceman.shape("spaceman.gif")
spaceman.penup()
spaceman.goto(-103,255)


space.addshape("rocket.gif")

rocket=turtle.Turtle()
rocket.shape("rocket.gif")
rocket.penup()
rocket.goto(180,-250)


def up():
    rocket.setheading(90)
    rocket.forward(10)
    rocket.setheading(0)

def down():
    rocket.setheading(270)
    rocket.forward(10)
    rocket.setheading(0)

def left():   
    rocket.setheading(180)
    rocket.forward(10)
    rocket.setheading(0)

def right():
    rocket.forward(10)

turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")

turtle.listen()

while True:
    space.update()
    if rocket.distance (spaceman) < 10 :
            space.bgpic("Thankyou.gif")


turtle.done()
