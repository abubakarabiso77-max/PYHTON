import turtle

# create screen
screen = turtle.screen()
screen.setup(width=600,height=600)
screen.bgcolor(lightblue)
screen.title(Drawing a square)

# create pen
pen = pen.screen
pen.color("black")
pen.pensize(3)

# Draw a square
for i in range (4):
    pen.forward(100)
    pen.right(90)

# keep the window open
turtle.done()