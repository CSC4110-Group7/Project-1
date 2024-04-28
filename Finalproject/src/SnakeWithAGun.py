import turtle
import time
import random
import math


delay = 0.1

# Score
score = 0
high_score = 0

#Bad News, I have to fundamentally rewrite Snake With A Gun to be more friendly for multiple objects being spawned
#The new plan is to have all objects be stored in a master list
#the master list will then have functions for checking collision (leading to death, bisection, or growth)
#the master list will then render every object in the master list after collision checking has been completed

ML = [] #this is the master list, where all objects to be rendered are spawned, they will be stored in a rendering engine
#object lists will be composed of the following
#ML[][0] = ID (if ID is same, don't check for collision for bullets, its a waste of time), if the ID is negative, it is a bullet ABS of ID will return snake that fired it, player is 1 
#ML[][1] = direction (this is the direction the snake is moving, if a snake becomes bisected, its copy consisting of all points past the bisection
# must also have the same direction)
#Direction for the AI snakes will be based on blindly aiming for the food by adjusting their x and y, AI snakes should have a 'look ahead' to determine when to turn
#ML[][2] = Speed
#ML[][3] = [Segment list]
#ML[][4] = color
#ML[][5] = uniqueID - this is the unique identifier of this particular object
#ML[][6] = [] Turnlist This is to prevent a snake from making 3 of the same turns in a row (this would mean death!)

#SnakeHeadInternals
MOVESPEED = 20 #note, movespeed can also be used to determine the size of the snakes, as long as movespeed and size are the same, a pixel grid is effectively created
WIDTH = 600
HEIGHT = 600
BORDERTOP = (HEIGHT - MOVESPEED*2)/2
BORDERSIDE = (WIDTH - MOVESPEED*2)/2
uniqueID = 0 #this is the unique idenfitier, it counts linerarly! I am truly a genius


#=-=-=-=-=-=-=-SPEED AND SCOREBOARD=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-
# Set up the screen
wn = turtle.Screen()
wn.title("Snake - WITH A GUN!")
wn.bgcolor("black")
#I regret using solid numbers here, in hindsight I should've set these as constants 
#and then adjusted values accordingly
wn.setup(width=WIDTH, height=HEIGHT)
wn.tracer(0)  # Turns off the screen updates

# Create Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0, 100)



#=-=--=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#HERE IS WHERE I NEED TO START RETHINKING ALL OF THIS
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#Create turtle objects using constructors of the turtle class.


#Segment list (this is where the additional segments go)


# Pen (this writes the actual font and whatnot)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

#Scoreboard
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Functions

#the collision engine checks for all possible collision events:
#border
#other snake segment
#food
#bullet



#the turtle killer is used when an object in a list is no longer needed
#and the turtle needs to be deleted
#it hides ALL turtle segments in the list
killList = []
#create a list of items to remove from the list so as to not interrupt the engine functions
def turtleKiller(UID):
    global killList
    killList.append(UID)
#called every pass to remove all indexes marked for termination
def turtleTerminator():
    global killList
    for UID in killList:
        for i in range (len(ML)-1,-1,-1):
            if UID == ML[i][5]:
                print("Head Position at time of death:")
                print("X: ", ML[i][3][0].xcor(), " Y: ", ML[i][3][0].ycor())
                for j in range(len(ML[i][3])-1,-1,-1):
                    ML[i][3][j].hideturtle()
                    ML[i][3][j].clear()
                del ML[i]
                continue
            
            if len(ML[i][3]) == 0:
                del ML[i]
                continue

    killList.clear()

def increaseLength(ID):
    ID = abs(ID)
    for i in range(0,len(ML)):
        if ID == ML[i][0]:
            
            if (len(ML[i][3]) == 0):
                continue
            
            print("Increasing length!")
            ns = turtle.Turtle()
            ns.speed(0)
            ns.shape("square")
            ns.color(ML[i][4])
            ns.penup()
            last_segment = ML[i][3][-1]
            ns.goto(last_segment.xcor(),last_segment.ycor())
            ML[i][3].append(ns)

def bisectSnake(j = -1,k = -1):
    if j == -1:
        return
    #j represents the index in ML of the snake
    #k represents the index in ML[3] of where the bisection occured. 
    global uniqueID
    segList = []
    #create a new unique ID for the new snake to be added to the ML
    uniqueID += 1
    tempcolor = random.choice(["blue", "pink", "orange"])
    tempdir = ML[j][1]
    tempINDEX = 0
    
    """
    #create a copy of the original, we will append this
    copyOriginal = ML[j].copy()
    copyOriginal[3].clear()
    
    copyOriginalIndex = 0
    #ML.append(copyOriginal)
    """
    copyOriginalID = ML[j][0]
    

    if (k == 0) or ((k+1) ==0):
        turtleKiller(copyOriginalID)
        return
    elif k == len(ML[j][3]):
        return
    
    #append a blank list version
    ML.append([uniqueID, tempdir, MOVESPEED, [], tempcolor, uniqueID, []])
    print("J is ", j, " k is ", k)
    print("Length of bisection target is: ", len(ML[j][3]))
    
    #find the index position of our newly added blank snake
    for ii in range(0,len(ML)):
        if uniqueID == ML[ii][0]:
            tempINDEX = ii
        
        if copyOriginalID == ML[ii][0]:
            copyOriginalIndex = ii
        
    
    
    
    
    
    for l in range(len(ML[j][3])-1,-1,-1):
        if (l == k) or (l == (k+1)):
            print("Point of intersection, deleting... k=", k , " l=",l)
            #if this is the point of intersection, remove the target position
            ML[j][3][l].hideturtle() 
            ML[j][3][l].clear()
            del ML[j][3][l]
            #if this is the in BLELOW of the point of intersection
            #first, copy the turtle object, place it in a new object,
            #and put that new turtle object in a list
        elif l > (k+1):
            print("Trying to create clone")
            #copy the original
            tempTurtle = turtle.Turtle()
            tempTurtle.speed(0)
            tempTurtle.shape("square")
            tempTurtle.color(tempcolor)
            tempTurtle.penup()
            tempTurtle.goto( ML[j][3][l].xcor(),ML[j][3][l].ycor() )
            ML[tempINDEX][3].insert(0,tempTurtle)
            #kill the original
            ML[j][3][l].hideturtle()
            ML[j][3][l].clear()
            del ML[j][3][l]
        """elif l < k:
            
            print("Trying to create clone")
            #copy the original
            tempTurtle = turtle.Turtle()
            tempTurtle.speed(0)
            tempTurtle.shape("square")
            tempTurtle.color("orange")
            tempTurtle.penup()
            tempTurtle.goto( ML[j][3][l].xcor(),ML[j][3][l].ycor() )
            ML[copyOriginalIndex][3].insert(0,tempTurtle)
            #kill the original
            ML[j][3][l].clear()
    #turtleKiller(copyOriginalID)
    """


def collisionEngine():
    
    #print("Is this working?")
    global score
    global uniqueID
    for i in range(len(ML)-1,-1,-1):
        
        #print("Is this thing even on???")
        #get the variables for the position of the head
        #print("I am attempting to get the i coordinate for this object in ML")
        if(i > len(ML)):
            print("Current I is ", i)
            continue
        elif len(ML[i][3]) ==0:
            print("Blank error, your clone from bisection spawned faulty!")
            continue
        
        xcor = ML[i][3][0].xcor()
        ycor = ML[i][3][0].ycor()
        ID = ML[i][0]
        UID = ML[i][5]
        amIdead = 0
        
        #Collision with wall check
        if ((xcor > BORDERTOP) or (xcor < -BORDERTOP) or (ycor > BORDERSIDE) or (ycor < -BORDERSIDE)):
            #if the player ID is detected, gameover
            if ID == 1:
                #note, please actually create the gameover function
                gameOver()
            print("ID", ID,  "have collided with the border!")
            amIdead = 1
            turtleKiller(UID)
            continue
        #Collision with self check
        if amIdead == 0:
            for j in range(1, len(ML[i][3])):
                #print(ML)
                #print(j)
                #print(i)
                if ML[i][3][j].distance(ML[i][3][0]) < MOVESPEED:

                    print("ID", ID,  "have collided with myself")
                    print("Collision distance: " , ML[i][3][j].distance(ML[i][3][0]))
                    print("My direction was: ", ML[i][1])
                    if ID > 1:
                        bisectSnake(i,j)
                    amIdead = 1
                    turtleKiller(UID)

                    if ID == 1:
                        gameOver()
                    break
        #Collision with everyone else check
        #make sure we aren't dead
        if amIdead == 0:
            for j in range(len(ML)-1,-1,-1):
                #If I'm scanning myself or one of my bullets, skip scan
                if (ML[j][0] == ID or ML[j][0] == -ID):
                    continue
                
                #Check through the array of all segments of foreign entity
                #additional self kill check
                if amIdead == 0:
                    for k in range(len(ML[j][3])-1,-1,-1):
                        #if the distance from myself to the enemy is less than the grid size, a collision has occured
                        #additional self kill check
                        if amIdead == 0:
                            if ML[j][3][k].distance(ML[i][3][0]) < MOVESPEED:
            
                                print("ID", ID,  "have collided with someone else! ID: ", ML[j][0] )
                                print("Collision distance: " , ML[j][3][k].distance(ML[i][3][0]))
                                #if I am a bullet, delete the segment I collided with, and bisect the rest of the list.
                                if ID != 1:
                                    print("I am a bullet")
                                    #if I am not just slicing off the tail.
                                    if 0 <= k < len(ML[j][3]):

                                        print("Bisecting!")
                                        bisectSnake(j,k)
                                                
                                #I have hit something that isn't myself, delete myself
                                turtleKiller(UID)
                                amIdead = 1
                                if ID == 1:
                                    gameOver()  
                                break
        #Collision with food check
        #print("Error Check, here is ML:")
        #print(ML)
        #check to see if what I am looking for even exists, otherwise an error will be thrown.
        if amIdead == 0:
            if ML[i][3][0].distance(food) < MOVESPEED:
                print("Food collision detected")
                if ID == 1:
                    score += 10
                    scoreUpdate()
                if ID < 0:
                    turtleKiller(UID)
                increaseLength(ID)
                #move the foods location, clear the old food.
                randx = random.randint(int(-BORDERSIDE),int(BORDERSIDE))
                randy = random.randint(int(-BORDERTOP),int(BORDERTOP))
                food.goto(randx, randy)
                

#the move engine elegantly renders every single object in the master list.
def moveEngine():
    fycor = food.ycor()
    fxcor = food.xcor()
    
    for i in range(0,len(ML)):
        
        if(len(ML[i][3]) == 0):
            continue
        
        ID = ML[i][0]
        idirection = ML[i][1]
        xcor = ML[i][3][0].xcor()
        ycor = ML[i][3][0].ycor()
        iMOVESPEED = ML[i][2]

        #AI nonsense ID greater than one means it is a computer
        if ID > 1:
            goodDirectionSet = {"up", "down", "left", "right"}#the banned direction list is a set of banned directions, whichever is left that isn't present will 
            #the direction we are already heading CANNOT be the way we go. 
            
            #Whichever direction is the opposite of which we are heading should be discarded
            if idirection == "up":
                goodDirectionSet.discard("down")
            elif idirection == "down":
                goodDirectionSet.discard("up")
            elif idirection == "right":
                goodDirectionSet.discard("left")
            elif idirection == "left":
                goodDirectionSet.discard("right")
            
            notBackSet = goodDirectionSet.copy()
            
            #We are not allowed to make 3 of the same turns in a row
            #if the list is 3 long or greater, begin check
            if len(ML[i][6]) >= 3:
                turnlist = ML[i][6]
                allturnset = {"up", "down", "left", "right"}
                turnset = set(turnlist)
                #if all three turns are unique, then whatever turn wasn't made would complete
                #a square
                #print("The last 3 turns were: ", turnlist)
                
                
                if len(turnset) == 3:
                    forbiddenturnset = allturnset.difference(turnset)
                    LEFTNEARBORDER = -BORDERSIDE + MOVESPEED
                    RIGHTNEARBORDER = BORDERSIDE - MOVESPEED
                    UPNEARBORDER = BORDERSIDE -MOVESPEED
                    DOWNNEARBORDER = BORDERSIDE + MOVESPEED
                    if not(xcor <= LEFTNEARBORDER or xcor >= RIGHTNEARBORDER or
                        ycor <= DOWNNEARBORDER or ycor >= UPNEARBORDER):
                        for forbiddendirection in forbiddenturnset:
                            goodDirectionSet.discard(forbiddendirection)
                            #print("The forbidden direction is: ", forbiddendirection)
                



            
            
            
            
            prefferedSet = set()
                        #be the chosen direction
            #Basic AI movement pattern, align with the food and move towards it
            #Might make sense to swap this for a random number generator to pick which choice
            #to make so that it generally moves towards the food but still can be dumb and hit
            #the wall
            #BASIC STEERING
            #These bands represent points on the board where the snake is aligned with the target
            LEFTBAND = fxcor - MOVESPEED
            RIGHTBAND = fxcor + MOVESPEED
            UPBAND = fycor + MOVESPEED
            DOWNBAND = fycor - MOVESPEED
            
            #figure out what SHOULD be the best way to go.
            if (xcor < LEFTBAND):
                prefferedSet.add("right")
            if xcor > RIGHTBAND:
                prefferedSet.add("left")
            if (ycor > UPBAND):
                prefferedSet.add("down")
            if (ycor < DOWNBAND):
                prefferedSet.add("up")
            
            #for remaining directions, figure out which directions we CANNOT go
            for direction in goodDirectionSet.copy():
                #print("Checking the future for the direction: ", direction)
                #print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                #calculate where we WILL be:
                #create fake values so it actually works
                futurexcor = xcor
                futureycor = ycor
                #print("Internal movespeed is: ", iMOVESPEED)
                if direction == "up":
                    futureycor = (ycor + iMOVESPEED)
                if direction == "down":
                    futureycor =(ycor - iMOVESPEED)
                if direction == "right":
                    futurexcor = (xcor + iMOVESPEED)
                if direction == "left":
                    futurexcor =(xcor - iMOVESPEED)
                
                    
                #Based on the direction iterated, figure out if we CANNOT head that way.
                #WALL LOOKAHEAD 
                #because we can only head in one direction at a time, if we discard ANY
                #direction, it means we don't need to iterate over it
                if (futurexcor > BORDERSIDE):
                    goodDirectionSet.discard("right")
                if (futurexcor < -BORDERSIDE):
                    goodDirectionSet.discard("left")
                if (futureycor > BORDERTOP):
                    goodDirectionSet.discard("up")
                if (futureycor < -BORDERTOP):
                    goodDirectionSet.discard("down")
                    
                #SELF COLLISION LOOK AHEAD
                #iterate through the self list DO NOT CHECK DISTANCE FROM HEAD
                for j in range(3,len(ML[i][3])):
                    #print("Attempting self collision lookahead")
                    #check the position of current course, change course if collision imminent
                    sxcor = ML[i][3][j].xcor()
                    sycor = ML[i][3][j].ycor()
                    #distance formula 
                    #if the distance between the future coordinates and a particular segment reveals collision CHANGE COURSE
                    #print("Segment Coordinates: X:", sxcor, " Y:", sycor)
                    #print("Future Head Coordinates: X: ", futurexcor, " Y:", futureycor)
                    
                    #print("Calulated distance: " ,math.sqrt((futurexcor - sxcor)**2 + (futureycor - sycor)**2))
                    if math.sqrt((futurexcor - sxcor)**2 + (futureycor - sycor)**2) < MOVESPEED:
                        
                        #print("Self collision future predicted, discarding:", direction)
                        goodDirectionSet.discard(direction)
                
                #Other collision lookahead
                for ii in range(len(ML)-1,-1,-1):
                    if ML[ii][0] != ID:
                        for j in range(len(ML[ii][3])-1,-1,-1):
                            #print("Attempting Other collision lookahead")
                            #check the position of current course, change course if collision imminent
                            sxcor = ML[ii][3][j].xcor()
                            sycor = ML[ii][3][j].ycor()
                            #distance formula 
                            #if the distance between the future coordinates and a particular segment reveals collision CHANGE COURSE
                            #print("Segment Coordinates: X:", sxcor, " Y:", sycor)
                            #print("Future Head Coordinates: X: ", futurexcor, " Y:", futureycor)
                            
                            #print("Calulated distance: " ,math.sqrt((futurexcor - sxcor)**2 + (futureycor - sycor)**2))
                            if math.sqrt((futurexcor - sxcor)**2 + (futureycor - sycor)**2) < MOVESPEED:
                                
                                #print("Self collision future predicted, discarding:", direction)
                                goodDirectionSet.discard(direction)

            


            
            #Figure out the intersect between the two sets.
            #Remember: the goodDirection set is all choices that will NOT lead to collisions
            #The preffered direction set is all choices that will get us closer to the objective
            #the valid direction set is all choices that are both GOOD and IDEAL
            #the NotBackSet is all choices that don't involve going where we have been
            #print("The preffered direction set is: ", prefferedSet)
            #print("The good direction set is: ", goodDirectionSet)
            validDirectionSet = prefferedSet.intersection(goodDirectionSet)
            #print("Valid directions calculated: ",validDirectionSet)
            

            #if there ARE valid choices (the best ones), pick from those
            beSilly = random.randint(0,30)
            
            if beSilly == 1:
                print("Behaving erratically on purpose! Choosing a good direction")
                ML[i][1] = random.choice(list(goodDirectionSet))
            
            elif (len(validDirectionSet) >0):
                #print("Attempting to pick first IDEAL direction")
                if idirection not in list(validDirectionSet):
                    ML[i][1] = list(validDirectionSet)[0]
            #if there are NO valid directions to go, pick randomly from the LEGAL direction set.
            #IF The good direction set even exists
            elif (not validDirectionSet) and (len(goodDirectionSet)>0) :
                #print("No ideal directions, picking from gooddirectionset:", goodDirectionSet)
                #print("Current direction: ", idirection)
                #default to the current direction if it is legal, otherwise we squiggle like crazy
                if idirection not in list(goodDirectionSet):
                    ML[i][1] = random.choice(list(goodDirectionSet))
            #if somehow both sets are empty, flail around randomly and hope it works out
            else:
                #print("There are no IDEAL choices, and no GOOD choices, flail about")
                ML[i][1] = random.choice(list(notBackSet))
                

                
            

            

            
            


            
                
                
            
            
        #Now that direction has been chosen, implement it        
        direction = ML[i][1]
        #if the direction is different, a turn has been made, pop it from the list
        if direction != idirection:
            ML[i][6].append(direction)
            if len(ML[i][6])>3:
                ML[i][6].pop()
        #Change the position of the head based upon direction
        xcor = ML[i][3][0].xcor()
        ycor = ML[i][3][0].ycor()

        
        #go through the list in reverse order to move up position of segments
        #segments adopt the position of the segments ahead of them
        for index in range(len(ML[i][3])-1, 0, -1):
            x = ML[i][3][index - 1].xcor()
            y = ML[i][3][index - 1].ycor()
            ML[i][3][index].goto(x, y)
        
        #THE HEAD MUST BE ADJUSTED AFTER THE REST OF THE LIST
        #OR ELSE WHEN A NEW PIECE IS ADDED TO THE LIST IT COLLIDES
        #IMMEDIATELY WITH THE PIECE AHEAD OF IT WHEN IT ADOPTS ITS 
        #COORDINATES DO NOT MOVE THIS IT MUST BE LAST
        if direction == "up":
            ML[i][3][0].sety(ycor + iMOVESPEED)
        elif direction == "down":
            ML[i][3][0].sety(ycor - iMOVESPEED)
        elif direction == "right":
            ML[i][3][0].setx(xcor + iMOVESPEED)
        elif direction == "left":
            ML[i][3][0].setx(xcor - iMOVESPEED)
            
        
#Player direction related functions, these determine the players direction in the player list
#Please note that the direction CANNOT be set to the opposite of the player's current direction, that would cause
#the snake to collide with itself, to prevent this impossibility a check is provided
def go_up():
        for i in ML:
            if i[0] == 1:
                if i[1] != "down":
                    i[1] = "up"
def go_down():
        for i in ML:
            if i[0] == 1:
                if i[1] != "up":
                    i[1] = "down"
def go_left():
        for i in ML:
            if i[0] == 1:
                if i[1] != "right":
                    i[1] = "left"
def go_right():
        for i in ML:
            if i[0] == 1:
                if i[1] != "left":
                    i[1] = "right"

shoot_now = 0

def shootActivate():
    global shoot_now
    shoot_now = 1
def shoot():
    global uniqueID
    global shoot_now
    if shoot_now == 1:
        #find the head of the snake that fired the shot
        #move the initial position to that of that snake
        for i in range(0,len(ML)):
            if ML[i][0] == 1:
                xcor = ML[i][3][0].xcor()
                ycor = ML[i][3][0].ycor()
                direction = ML[i][1]
        
        #create turtle object
        bullet = turtle.Turtle()
        bullet.speed(0)
        bullet.shape("square")
        bullet.color("red")
        bullet.penup()
        #when created, go to the headcoordinates of the creator
        bullet.goto(xcor, ycor)
        
        #add the new bullet to the bulletlist for the bullet renderer to handle (create a new object in the master list tbh)
        ML.append([-1, direction, MOVESPEED*1.5, [bullet],"red", uniqueID,[]])
        uniqueID += 1 #increase the value of the unique ID so no other Unique IDs are created
        shoot_now = 0
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-




#=-=-=-=-=-=-=-=-=-=-GAME OVER
def gameOver():
    """
    pen.clear()
    pen.write("GAME OVER", align="center",font=("Impact", 55, "normal"))
    wn.update()
    time.sleep(3)
    
    pen.clear()
    scoreUpdate()
    resetGame()
    """
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def resetGame():
    # Reset the score
    score = 0

    # Reset the delay
    delay = 0.1
    
    #Clear the ML
    ML.clear()
    
    # Create Snake fooda
    food.goto(0, 200)
    
    
    
    
    #Fill the ML
    player = turtle.Turtle()
    player.speed(0)
    player.shape("square")
    player.color("yellow")
    player.goto(0,0)
    player.penup()
    playerlist = [1, "up", MOVESPEED, [player], "yellow",-1,[]]
    ML.append(playerlist)
    
    enemy = turtle.Turtle()
    enemy.speed(0)
    enemy.shape("square")
    enemy.color("purple")
    enemy.goto(0,MOVESPEED)
    enemy.penup()
    enemylist = [2,"up", MOVESPEED, [enemy], "purple", -2,[]]
    ML.append(enemylist)
    
    
#Score update function 
def scoreUpdate():
    #if score > high_score:
        #high_score = score
    #pen.clear()
    #pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
     #                 font=("Impact", 24, "normal"))
    print("scoreUpdated")


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Keyboard bindings
#This is the bit where movement is actually detected
target = -1
def pickTarget(i):
    print("Target picked!")
    global target
    target = i
    
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(lambda: bisectSnake(target, 4), "b")
wn.onkeypress(lambda: pickTarget(1), "1")
wn.onkeypress(lambda: pickTarget(0), "0")
wn.onkeypress(shootActivate, "space")  #shoot!


    
    

#=-=-=-=-=-=-=-=-=-=-=-=-=-=--




# Main game loop
resetGame()
while True:
    wn.update()
    moveEngine()
    collisionEngine()
    turtleTerminator()
    shoot()
    time.sleep(delay)

wn.mainloop()
