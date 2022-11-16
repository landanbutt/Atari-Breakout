import turtle



wn = turtle.TurtleScreen()

def main():

    name = input("What's your name?: ")

    if name == "landan":
        print("gay")

wn.listen()
wn.onkeypress(main, "space")
