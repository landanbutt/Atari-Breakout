import turtle
import config
life_count = 3


# Window Screen

wn = turtle.Screen()
wn.title("Atari Breakout")
wn.bgcolor("black")
wn.setup(width=1200, height=800)
wn.tracer(1)
turtle.colormode(255)


# Life Count Display

life_counter = turtle.Turtle()
life_counter.speed(0)
life_counter.shape("square")
life_counter.color(0, 125, 200)
life_counter.penup()
life_counter.hideturtle()
life_counter.goto(-450, -375)
life_counter.write(life_count * "_ ", align="center", font=("Courier", 48, "normal"))


# Paddle

paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.shapesize(stretch_len=6, stretch_wid=0.5)
paddle.color(0, 125, 200)
paddle.penup()
paddle.goto(0, -330)


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


# Game Start

def play_on():
    global play
    play = True
    print("play")
play = False

wn.listen()
wn.onkeypress(paddle_left, "a")
wn.onkeypress(paddle_right, "d")
wn.onkeypress(play_on, "space")


# Main Game Loop

while life_count > 0 and play == True:
    wn.update()

    # Ball Movement

    ball.dx = config.ballx_move_speed
    ball.setx(ball.xcor() + ball.dx)

    ball.dy = config.bally_move_speed
    ball.sety(ball.ycor() + ball.dy)

    # Left and Right Bounce

    if ball.xcor() > 590:
        ball.setx(590)
        config.ballx_move_speed *= -1
    elif ball.xcor() < -590:
        ball.setx(-590)
        config.ballx_move_speed *= -1

    # Top and Bottom Bounce

    if ball.ycor() > 390:
        ball.sety(390)
        config.bally_move_speed *= -1
    elif ball.ycor() < -345:
        ball.goto(0, 0)
        life_count -= 1
        life_counter.clear()
        life_counter.write(life_count * "_ ", align="center", font=("Courier", 48, "normal"))

    # Paddle Bounce

    if (ball.ycor() < paddle.ycor() + 10) and ((ball.xcor() < paddle.xcor() + 65) and
                                               (ball.xcor() > paddle.xcor() - 65)):

        ball.sety(paddle.ycor() + 10)
        config.bally_move_speed *= -1








wn.exitonclick()