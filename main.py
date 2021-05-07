from background import *
import subprocess
import turtle
from tkinter import *


FILE_NAME = "ALTurtle"

screen = turtle.Screen()
screen.bgcolor('black')
turtle.speed(0)
draw_background()

import studentspiral

turtle.ht()

screen.getcanvas().postscript(file=f"{FILE_NAME}.eps")

subprocess.run(["inkscape", f"--export-filename={FILE_NAME}.svg", f"{FILE_NAME}.eps"])
subprocess.run(["rm", f"{FILE_NAME}.eps"])
