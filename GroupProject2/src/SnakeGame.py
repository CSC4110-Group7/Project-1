import turtle
import tkinter as tk
import time

def drawRect(turtle, x, y, w, h, color, fill_color):
    turtle.up()
    turtle.goto(x, y)
    turtle.setheading(0) #Make the turtle face +x (right)
    turtle.fillcolor(fill_color)
    turtle.color(color)
    turtle.begin_fill()
    turtle.down()
    turtle.speed(0)
    
    for _ in range(2):
        turtle.forward(w)
        turtle.right(90)
        turtle.forward(h)
        turtle.right(90)

    turtle.end_fill()

TILE_WIDTH = 10
UPDATE_TIME = 0.05

class GameObject:
    def __init__(self, x=0, y=0, vx=0, vy=0, w=10, h=10):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.w = w
        self.h = h

        self.color = "black"

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def render(self, turtle):
        drawRect(turtle, self.x, self.y, self.w, self.h, self.color, self.color)
        
class Snake(GameObject):
    def __init__(self, color, x, y):
        super().__init__(x, y, 1 * TILE_WIDTH, 0, TILE_WIDTH, TILE_WIDTH)
        self.color = color
        self.length = 3
        
        self.segments = []
        
    def update(self):
        self.segments.append(SnakeSegment(self.x, self.y, self.color))
        
        if(len(self.segments) > self.length):
            self.segments.pop(0)
            
        super().update()
        
    def render(self, turtle):
        for segment in self.segments:
            segment.render(turtle)
        
class SnakeSegment(GameObject):
    def __init__(self, x, y, color):
        super().__init__(x, y, 0, 0, TILE_WIDTH, TILE_WIDTH)
        self.color = color

class Game:
    def __init__(self, root):
        self.update_time = 500
        self.paused = True
        self.running = True
        self.width = 500
        self.height = 500

        self.root = root
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.turtle = turtle.RawTurtle(self.canvas)
        self.turtle.hideturtle()
        self.turtle.speed(0)
        self.turtle.getscreen().tracer(0)

        self.objects = []
        self.objects.append(Snake("red", 40, 40))
        
    def start(self):
        while self.running:
            self.update()
            self.render()
            self.turtle.getscreen().update()
            time.sleep(UPDATE_TIME)
            

    def update(self):
        if(self.paused):
            return
        
        for object in self.objects:
            object.update()

    def render(self):
        self.turtle.clear()
        
        for object in self.objects:
            object.render(self.turtle)
            

    def addObject(self, object):
        self.objects.append(object)

    def init(self):

        self.update()

    def unpause(self):
        self.paused = False
    def pause(self):
        self.paused = True


