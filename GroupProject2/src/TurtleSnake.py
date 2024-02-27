import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

#Bullets list (to be rendeturtleturtle
#SnakeHeadInternals
bullets = []

MOVESPEED = 20

#=-=-=-=-=-=-=-SPEED AND SCOREBOARD=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-
# Set up the screen
wn = turtle.Screen()
wn.title("Snake - WITH A GUN!")
wn.bgcolor("black")
#I regret using solid numbers here, in hindsight I should've set these as constants 
#and then adjusted values accordingly
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates



#Score update function
def scoreUpdate(score, high_score):
    if score > high_score:
        high_score = score
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Impact", 24, "normal"))
#=-=--=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Create turtle objects using constructors of the turtle class.
# Snake head
   
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0, 100)

#Segment list (this is where the additional segments go)
segments = []

# Pen (this writes the actual font and whatnot)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

#Scoreboard
scoreUpdate(score, high_score)
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    #Gets the current coordinate for x or y, then adjusts it 
    #based on the move constant. Currently I have hardcoded
    #it for 20, that should be adjusted to adjust game difficulty?
    #maybe make it in the future so that speed increases as length increases
    #Update: added in constants
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + MOVESPEED)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - MOVESPEED)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - MOVESPEED)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + MOVESPEED)
def shoot():
    bullet = turtle.Turtle()
    bullet.speed(0)
    bullet.shape("square")
    bullet.color("red")
    bullet.penup()
    bullet.goto(head.xcor(), head.ycor())
    bullet.direction = head.direction
    #add the new bullet to the bulletlist for the bullet renderer to handle
    bullets.append(bullet)
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Keyboard bindings
#This is the bit where movement is actually detected

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(shoot, "space")  #shoot!
#=-=-=-=-=-=-=-=-=-=-=-=-=-=--

#=-=-=-=-=-=-=-=-=-=-GAME OVER
def gameOver(head,segment,score,high_score,delay,pen):
    pen.clear()
    pen.write("GAME OVER", align="center",font=("Impact", 55, "normal"))
    wn.update()
    time.sleep(3)
    
    head.goto(0, 0)
    head.direction = "stop"

    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)

     # Clear the segments list
    segments.clear()

    # Reset the score
    score = 0

    # Reset the delay
    delay = 0.1
    pen.clear()
    scoreUpdate(score, high_score)
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


# Main game loop
while True:
    wn.update()

    #-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-
    # Check for a collision with the border THIS MEANS THE PLAYER LOSES!!!!!!
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
       gameOver(head,segment,score,high_score,delay,pen)
        
    # Check for head collisions with body segments THIS MEANS THE PLAYER LOSES!!!!!
    for segment in segments:
        if segment.distance(head) < 20:
            gameOver(head,segment,score,high_score,delay,pen)
    #-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-00


    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        #SEGMENT SECTION (the bit where the parts behind the turtle are spawned)
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10
        pen.clear()
        scoreUpdate(score, high_score)

    # Move the end segments first in reverse order
    #because the oldest segments are at the RIGHT end of the list and thus should be moved first
    for index in range(len(segments) - 1, 0, -1):
        #the new segments position is based on the the position of the prior segment
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    
    #--0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0
    # Bullets are actually moved here
    #BULLET RENDERING
    #Go through the the bullet list, get the direction of the bullet turtle object, 
    # adjust its position based on the move speed
    for bullet in bullets:
        if bullet.direction == "up":
            bullet.sety(bullet.ycor() + int(MOVESPEED*1.5))
        elif bullet.direction == "down":
            bullet.sety(bullet.ycor() - int(MOVESPEED*1.5))
        elif bullet.direction == "left":
            bullet.setx(bullet.xcor() - int(MOVESPEED*1.5))
        elif bullet.direction == "right":
            bullet.setx(bullet.xcor() + int(MOVESPEED*1.5))

    # Check for bullet collision with food (I really regret not making a universal checker for this function)
    for bullet in bullets:
        #Bullet if bullet hits food
        if bullet.distance(food) < 20:
            #moves the food (Maybe I can make this a function?)
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)
            #=-=-=-=-=-=-=-=-=-=-=-=-=-=
            
            #you can shoot multiple bullets
            #The bullet hit the target, delete the bullet
            bullets.remove(bullet)
            bullet.hideturtle()
            
            score += 10

            pen.clear()
            scoreUpdate(score, high_score)
    # Check for bullet collision with border
        elif bullet.xcor() > 290 or bullet.xcor() < -290 or bullet.ycor() > 290 or bullet.ycor() < -290:
            #delete the bullet because it is beyond the rendering distance
            bullets.remove(bullet)
            bullet.hideturtle()
    #-0-0-0-0-0-0-0-0-0-0-0-0-0-0-00-0-0-0-0-0-0-0-0-0-




    time.sleep(delay)

wn.mainloop()
