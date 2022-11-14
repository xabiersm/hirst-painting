import random

import colorgram
import turtle as t

tim = t.Turtle()
t.colormode(255)
tim.speed(7)
colors = colorgram.extract('image.jpg', 30)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

# print(rgb_colors)
tim.penup()
tim.hideturtle()
tim.setposition(-200, -200)

for height in range(10):
    for width in range(10):
        tim.dot(20, random.choice(rgb_colors))
        # tim.setheading(0)
        tim.forward(50)
    tim.sety(tim.ycor() + 50)
    tim.setx(-200)

screen = t.Screen()
screen.exitonclick()