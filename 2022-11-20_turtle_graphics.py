import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("arrow")
tim.color("red")
tim.speed("fastest")

colors = ["red", "green", "blue", "orange", "black", "yellow", "purple", "brown"]
directions = [0, 90, 180, 270]


def draw_shape(num_sides):
    angel = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angel)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)


def random_walk(head_direction):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(head_direction))


tim.pensize(10)
for _ in range(100):
    random_walk(directions)

screen = Screen()
screen.exitonclick()