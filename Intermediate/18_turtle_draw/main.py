import colorgram
import random
import turtle as t

def get_colors(image, number_of_colors):
    """Return list with inserted numbers tuple of rgb colors from image."""
    colors = colorgram.extract(image, number_of_colors)
    rgb_list = []
    for color in colors:
        r = []
        for el in color.rgb:
            r.append(el)
        rgb_list.append(tuple(r))
    return rgb_list

def get_position(x, y):
    """Returs next position cordinate x,y."""
    if x == 0 and y == 0:
        return -325, -320
    elif x > 300:
        return -325, y + 70
    else:
        return x + 70, y

colors = get_colors("image.jpg", 10)

screen = t.Screen()
screen.setup(width=700, height=700)

t.colormode(255)
pen = t.Turtle()
pen.speed(0)
pen.up()
pen.hideturtle()



paint = True
while paint:
    x, y = get_position(pen.xcor(), pen.ycor())
    if y > 310:
        paint = False
    else:
        pen.goto(x, y)
        pen.dot(20, random.choice(colors[2:]))

screen.exitonclick()