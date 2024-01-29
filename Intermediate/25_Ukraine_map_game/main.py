import turtle


screen = turtle.Screen()
screen.title("Ukraine City Game")
screen.setup(width=0.7, height=0.75, startx=None, starty=None)
image = 'ua_map.gif'
screen.addshape(image)

turtle.shape(image)

def get_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_click_coor)
turtle.mainloop()

#screen.exitonclick()