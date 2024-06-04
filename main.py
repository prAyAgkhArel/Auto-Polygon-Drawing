from turtle import Turtle
timmy = Turtle()
timmy.pensize(width = 5)

import random
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#Drawing a shapes
for sides in range(3, 11):
    angle = 360/sides
    for n in range(sides):
        timmy.color(random.choice(colours))
        timmy.forward(75)
        timmy.left(angle)