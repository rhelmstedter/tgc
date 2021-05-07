import turtle


def draw_background():
    """ Draw a background rectangle. """
    ts = turtle.getscreen()
    canvas = ts.getcanvas()
    height = ts.getcanvas()._canvas.winfo_height()
    width = ts.getcanvas()._canvas.winfo_width()

    turtleheading = turtle.heading()
    turtlespeed = turtle.speed()
    penposn = turtle.position()
    penstate = turtle.pen()

    turtle.penup()
    turtle.speed(0)  # fastest
    turtle.goto(-width / 2 - 2, -height / 2 + 3)
    turtle.fillcolor(turtle.Screen().bgcolor())
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(width)
    turtle.setheading(90)
    turtle.forward(height)
    turtle.setheading(180)
    turtle.forward(width)
    turtle.setheading(270)
    turtle.forward(height)
    turtle.end_fill()

    turtle.penup()
    turtle.setposition(*penposn)
    turtle.pen(penstate)
    turtle.setheading(turtleheading)
    turtle.speed(turtlespeed)
