import colorgram

colors = colorgram.extract('image.jpg', 30)
rgb_colors: list[tuple] = []

for color in colors:
    r: int = color.rgb.r
    g: int = color.rgb.g
    b: int = color.rgb.b
    new_color: tuple = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

color_list: list[tuple] = [(35, 19, 15), (197, 144, 123), (30, 106, 155), (142, 85, 55), (9, 21, 45), (236, 213, 85), (196, 135, 155), (156, 62, 90), (221, 85, 66), (153, 17, 37), (202, 79, 104), (14, 54, 30), (162, 163, 35), (118, 172, 196), (41, 125, 79), (77, 12, 22), (120, 188, 160), (18, 92, 53), (11, 58, 137), (23, 201, 179), (23, 174, 206), (139, 222, 208), (149, 23, 16), (223, 172, 191), (233, 172, 162), (238, 206, 8)]
