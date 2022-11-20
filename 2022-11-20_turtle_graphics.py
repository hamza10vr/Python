import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.shape("arrow")
tim.speed("fastest")
directions: list[int] = [0, 90, 180, 270]


def random_color() -> tuple:
    r: int = random.randint(0, 255)
    g: int = random.randint(0, 255)
    b: int = random.randint(0, 255)
    rgb: tuple = (r, g, b)
    return rgb


def draw_shape(num_sides):
    angel = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angel)


for shape_side_n in range(3, 11):
    tim.color(random_color())
    draw_shape(shape_side_n)


def random_walk(head_direction):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(head_direction))


tim.pensize(10)
for _ in range(100):
    random_walk(directions)

screen = t.Screen()
screen.exitonclick()
