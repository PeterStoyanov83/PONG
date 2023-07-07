import turtle
import os


wn = turtle.Screen()
wn.title("Pong by Peter Stoyanov")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score System
score_a = 0
score_b = 0

# paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# PADDLE B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# pen for score

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#MAIN GAME LOOP

while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


# Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay pop_2.aiff&")
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay pop_2.aiff&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        os.system("afplay cheering_crowd_studio.aif&")
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        os.system("afplay cheering_crowd_studio.aif&")



# The Bounse!
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < (paddle_b.ycor() + 40) and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay pop_1.aif&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < (paddle_a.ycor() + 40) and ball.ycor() > paddle_a.ycor() -40 ):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay pop_1.aif&")


    if score_a == 10 or score_b == 10:
        wn.clear()
        wn.bgcolor("black")
        pen.clear()
        pen.write("G A M E   O V E R !", align="center", font=("Courier", 30, "normal"))
        if score_a > score_b:
            pen.write("P L A Y E R   A   W I N S !!!", align="down", font=("Courier", 30, "normal"))
        else:
            pen.write("P L A Y E R   B   W I N S !!!", align="down", font=("Courier", 30, "normal"))
        os.system("afplay game_over_cheer.aif&")

