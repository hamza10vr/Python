from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")

colors = ["red", "green", "blue", "orange", "black", "yellow", "purple", "brown"]


def draw_shape(num_sides):
    angel = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angel)


for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()