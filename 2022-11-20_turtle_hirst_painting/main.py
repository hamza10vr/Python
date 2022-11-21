# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors: list[tuple] = []
#
# for color in colors:
#     r: int = color.rgb.r
#     g: int = color.rgb.g
#     b: int = color.rgb.b
#     new_color: tuple = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle as t
color_list: list[tuple] = [(35, 19, 15), (197, 144, 123), (30, 106, 155), (142, 85, 55), (9, 21, 45), (236, 213, 85), (196, 135, 155), (156, 62, 90), (221, 85, 66), (153, 17, 37), (202, 79, 104), (14, 54, 30), (162, 163, 35), (118, 172, 196), (41, 125, 79), (77, 12, 22), (120, 188, 160), (18, 92, 53), (11, 58, 137), (23, 201, 179), (23, 174, 206), (139, 222, 208), (149, 23, 16), (223, 172, 191), (233, 172, 162), (238, 206, 8)]

t.colormode(255)
screen = t.Screen()
screen.setworldcoordinates(-1, -1, screen.window_width(), screen.window_height())
tim = t.Turtle()


def paint_a_line(colors):
    for _ in range(10):
        color = random.choice(colors)
        tim.pendown()
        tim.dot(20, color)
        tim.penup()
        tim.fd(50)


screen.title("Witness the Amazing Turtle Art")
for i in range(10):
    tim.setpos(0, i * 50)
    paint_a_line(color_list)

t.exitonclick()
