import turtle
import tkinter as tk

def drawRect(turtle, x, y, w, h, color, fill_color):
    turtle.up()
    turtle.goto(x, y)
    turtle.setheading(0) #Make the turtle face +x (right)
    turtle.fillcolor(fill_color)
    turtle.color(color)
    turtle.begin_fill()
    turtle.down()
    
    for _ in range(2):
        turtle.forward(w)
        turtle.right(90)
        turtle.forward(h)
        turtle.right(90)

    turtle.end_fill()

class GameObject:
    def __init__(self, x=0, y=0, vx=0, vy=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.color = "white"

    def update(self):
        pass

    def render(self, turtle):
        drawRect(turtle, self.x, self.y, self.color, self.color)


class Game:
    def __init__(self, root):
        self.update_time = 500
        self.paused = True

        self.root = root
        self.turtle = turtle.Turtle()
        self.canvas = turtle.getcanvas()

        self.objects = []

        self.update()

    def update(self):
        if(self.paused):
            #self.root.after(self.update_time, self.update())
            return
        
        for object in self.objects:
            object.update()

        #self.root.after(self.update_time, self.update())
        

    def render(self):
        for object in self.objects:
            object.render(self.turtle)

    def addObject(self, object):
        self.objects.append(object)


