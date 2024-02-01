import csv
import turtle


screen = turtle.Screen()
screen.title("Ukraine City Game")
screen.setup(width=0.7, height=0.75, startx=None, starty=None)
image = 'ua_map.gif'
screen.addshape(image)

turtle.shape(image)

#def get_click_coor(x, y):
#    print(x, y)
#turtle.onscreenclick(get_click_coor)
#turtle.mainloop()

def get_city_data(city_input):
    name = city_input
    coor = cities_data[name]
    return name, coor

def create_city_turtle(name, coor): 
    city_turtle = turtle.Turtle()
    city_turtle.hideturtle()
    city_turtle.penup()
    city_turtle.goto(float(coor[0]), float(coor[1]))
    city_turtle.write(f"{name}", move=False, align="left", font=("Arial", 8, "normal"))



with open("ua_cities.csv", mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    cities_data = {row[0]:row[1:] for row in reader}

count = 0
while count != 25:
    answer_city = screen.textinput(title=f"{count}/25 Guess the City", 
                                   prompt="What's the city name? 'Exit' for exit=)").title()
    if answer_city == "Exit":
        break
    if answer_city in cities_data.keys():
        count += 1
        city_name, city_coor = get_city_data(answer_city)
        create_city_turtle(city_name, city_coor)
    
