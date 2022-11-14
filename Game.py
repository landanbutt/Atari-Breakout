import turtle
import config

# DEREK IS THE COOLEST
# Window Screen

wn = turtle.Screen()
wn.title("Atari Breakout")
wn.bgcolor("black")
wn.setup(width=1200, height=800)
wn.tracer(1)
turtle.colormode(255)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.shapesize(stretch_len=6, stretch_wid=0.5)
paddle.color(0, 125, 200)
paddle.penup()
paddle.goto(0, -350)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.color("grey")
ball.penup()
ball.goto(0, 0)

# Paddle Movement


def paddle_left():
    x = paddle.xcor()
    x -= config.paddle_move_distance
    paddle.setx(x)


def paddle_right():
    x = paddle.xcor()
    x += config.paddle_move_distance
    paddle.setx(x)


wn.listen()
wn.onkeypress(paddle_left, "a")
wn.onkeypress(paddle_right, "d")
























wn.exitonclick()





















