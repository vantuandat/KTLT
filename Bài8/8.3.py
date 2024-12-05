print("Sinh vien:Van Tuan Dat")
print("MSSV:235752021610083")
##################

import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle object
painter = turtle.Turtle()
painter.speed(0)
painter.pensize(2)

# List of colors
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

# Draw the overlapping circular pattern
for _ in range(12):  # 12 circles in total
    painter.color(random.choice(colors))
    painter.circle(100)  # Radius of the circle
    painter.right(30)    # Angle to shift for the next circle

# Hide the turtle
painter.hideturtle()

# Keep the window open
turtle.done()
