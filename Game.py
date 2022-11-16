import turtle
import config


# The total lives the user has to play with
global life_count
# A flag that signals if the user is playing a game
global play
# The window that is listening for input from the user
global wn
# The paddle the user plays with
global paddle
# The ball the user plays with
global ball
# DESCRIBE THIS PUSSY
global life_counter


# Sets up all the necessary variables for the game to function
def initialize_game_variables():

    global wn
    global paddle
    global ball
    global life_counter

    wn = turtle.Screen()
    paddle = turtle.Turtle()
    ball = turtle.Turtle()
    life_counter = turtle.Turtle()

    # Window Screen

    wn.title("Atari Breakout")
    wn.bgcolor("black")
    wn.setup(width=1200, height=800)
    wn.tracer(1)
    turtle.colormode(255)

    # Life Count Display

    life_counter.speed(0)
    life_counter.shape("square")
    life_counter.color(0, 125, 200)
    life_counter.penup()
    life_counter.hideturtle()
    life_counter.goto(-450, -375)
    life_counter.write(life_count * "_ ", align="center", font=("Courier", 48, "normal"))

    # Paddle

    paddle.speed(0)
    paddle.shape("square")
    paddle.shapesize(stretch_len=6, stretch_wid=0.5)
    paddle.color(0, 125, 200)
    paddle.penup()
    paddle.goto(0, -330)

    # Ball

    ball.speed(0)
    ball.shape("circle")
    ball.shapesize(stretch_len=1, stretch_wid=1)
    ball.color("grey")
    ball.penup()
    ball.goto(0, 0)


# Set up the window to listen for key presses from the user
def initialize_window():
    wn.onkeypress(paddle_left, "a")
    wn.onkeypress(paddle_right, "d")
    wn.onkeypress(play_on, "space")
    wn.listen()


# Paddle Movement

def paddle_left():
    x = paddle.xcor()
    x -= config.paddle_move_distance
    paddle.setx(x)


def paddle_right():
    x = paddle.xcor()
    x += config.paddle_move_distance
    paddle.setx(x)


# Resets the player's lives
def reset_lives():
    global life_count
    # Resetting the lives count since a new game is beginning
    life_count = 3
    life_counter.clear()
    life_counter.write(life_count * "_ ", align="center", font=("Courier", 48, "normal"))


# This function handles whenever the user presses the space bar, and attempts to start a new game
def play_on():
    # Only start a new game if one is not already in progress
    if not play:
        run_game_loop()


# This function contains the actual game logic, which is a loop that terminates when the user runs out
# of lives
def run_game_loop():
    # Declaring global variables, and setting the 'play' flag to true, since a game has begun
    global life_count
    global play
    play = True

    # Resetting the player's lives since a new game is beginning
    reset_lives()

    while life_count > 0:
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

    # At this point, the 'play' flag can be set to false, since we are out of the while loop
    # and the game is over
    play = False


# This is the function that drives the overall logic, it sets up the environment, and then controls
# the main flow of execution
def main():
    # Variable setup
    global play
    global life_count
    life_count = 3

    play = False

    # Game setup
    initialize_game_variables()
    initialize_window()

    # The game will now be run whenever the user presses the space bar,
    # as this will trigger the play_on() function which executes the main game loop

    # If the user ever clicks the screen, this will trigger this line, which will cause this main()
    # function to exit and the program to end
    wn.exitonclick()


# Executing the main game logic
main()
