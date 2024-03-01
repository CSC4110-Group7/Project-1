import turtle
import tkinter as tk
import time


def fillRect(turtle, x, y, w, h, color, fill_color, side_width=1):
    turtle.up()
    turtle.goto(x, y)
    turtle.setheading(0) #Make the turtle face +x (right)
    turtle.fillcolor(fill_color)
    turtle.pencolor(color)
    turtle.width(side_width)
    turtle.begin_fill()
    turtle.down()
    turtle.speed(0)
    
    for _ in range(2):
        turtle.forward(w)
        turtle.right(90)
        turtle.forward(h)
        turtle.right(90)

    turtle.end_fill()
    

# The width (in pixels) of each tile
TILE_WIDTH = 15

# The size of the play field in tile units
GRID_WIDTH = 40
GRID_HEIGHT = 30

# How much space should be around the play field (for text rendering or other)
SCREEN_PADDING = 20
SCREEN_PADDING_TOP = 100

# Actual screen size
SCREEN_WIDTH = TILE_WIDTH * GRID_WIDTH + (SCREEN_PADDING * 2)
SCREEN_HEIGHT = TILE_WIDTH * GRID_HEIGHT + (SCREEN_PADDING + SCREEN_PADDING_TOP)

# XY Coordinates of the beginning and end of the play field
GRID_BEGIN_X = SCREEN_PADDING - (SCREEN_WIDTH / 2)
GRID_BEGIN_Y = (SCREEN_HEIGHT / 2) - SCREEN_PADDING_TOP
GRID_END_X = SCREEN_PADDING + SCREEN_WIDTH
GRID_END_Y = SCREEN_PADDING + SCREEN_HEIGHT

# Time between updates
UPDATE_TIME = 0.05



class GameObject:
    def __init__(self, x=0, y=0, vx=0, vy=0, w=TILE_WIDTH, h=TILE_WIDTH):
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
        fillRect(turtle, self.x, self.y, self.w, self.h, self.color, self.color)
        
class Snake(GameObject):
    def __init__(self, color, tile_x, tile_y):
        super().__init__(
            tile_x * TILE_WIDTH + GRID_BEGIN_X, 
            tile_y * TILE_WIDTH + GRID_BEGIN_Y, 
            1 * TILE_WIDTH, 0
            )
        
        self.color = color
        self.length = 5
        
        self.segments = []
        
    def update(self):
        super().update()
        self.segments.append(SnakeSegment(self.x, self.y, self.color))
        
        if(len(self.segments) > self.length):
            self.segments.pop(0)
            
        
    def render(self, turtle):
        for i, segment in enumerate(self.segments):
            if i == len(self.segments)-1:
                segment.render(turtle, None)
            else:
                segment.render(turtle, self.segments[i-1])
                
        
SEGMENT_GAP = 2
class SnakeSegment(GameObject):
    def __init__(self, x, y, color):
        super().__init__(x, y, 0, 0)
        self.color = color
        
    def render(self, turtle, prev_segment):
        if(prev_segment == None):
            fillRect(turtle, self.x + SEGMENT_GAP, self.y + SEGMENT_GAP, self.w - (SEGMENT_GAP*2), self.h - (SEGMENT_GAP*2), self.color, self.color)
            return
    
        if(prev_segment.x < self.x):
            fillRect(turtle, self.x, self.y + SEGMENT_GAP, self.w - SEGMENT_GAP, self.h - (SEGMENT_GAP * 2), self.color, self.color)
        elif(prev_segment.x > self.x):
            fillRect(turtle, self.x + SEGMENT_GAP, self.y + SEGMENT_GAP, self.w - SEGMENT_GAP, self.h - (SEGMENT_GAP * 2), self.color, self.color)
        elif(prev_segment.y < self.y):
            fillRect(turtle, self.x + SEGMENT_GAP, self.y, self.w - (SEGMENT_GAP * 2), self.h - SEGMENT_GAP, self.color, self.color)
        else:
            fillRect(turtle, self.x + SEGMENT_GAP, self.y + SEGMENT_GAP, self.w - (SEGMENT_GAP * 2), self.h - SEGMENT_GAP, self.color, self.color)

class Game:
    def __init__(self, root):
        self.root = root
        self.paused = True
        self.running = True
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT

        self.root = root
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        self.turtle = turtle.RawTurtle(self.canvas)
        self.turtle.hideturtle()
        self.turtle.speed(0)
        
        # Disable window updates since we'll be taking it from here
        self.turtle.getscreen().tracer(0)

        # Create a list of game objects in play
        self.objects = []
        self.players = []
        
        # Create player 1
        player1 = Snake("green", 0, 0)
        self.players.append(player1)
        self.objects.append(player1)
        
        # Init controls for player1
        self.turtle.getscreen().onkeypress()
        
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
        
        # Draw a perimeter around the play area
        fillRect(self.turtle, 0, 0, TILE_WIDTH, TILE_WIDTH, "red", "white")
        fillRect(self.turtle, GRID_BEGIN_X, GRID_BEGIN_Y, GRID_WIDTH * TILE_WIDTH, GRID_HEIGHT * TILE_WIDTH, "black", "gray", 2)
        
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


