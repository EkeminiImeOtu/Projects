# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 07:14:41 2022 

@author: Mark

Snake
Complete the Snake project based on #TODO's. https://docs.python.org/3/library/turtle.html#module-turtle
"""
# TODO - import the packages: turtle, time and random
import turtle
import time
import random

#global variable
window = None
snake = []
head = None

direction = 'down'
delay_time = 0.85

food = None
food_color = ''

TURTLE_SIZE = 20
WIDTH = 500
HEIGHT = 500

X_RANGE = (WIDTH - TURTLE_SIZE) / 2
Y_RANGE = (HEIGHT - TURTLE_SIZE) / 2

pen = None
score = 0
high_score = 0

shapes = {
        0: 'turtle',
        1: 'classic',
        2: 'arrow',
        3: 'circle',
        4: 'square',
        5: 'triangle'
        } # TODO - define shapes dictionary

colors = {
        0: 'gold',
        1: 'lime green',
        2: 'dark magenta',
        3: 'light salmon',
        4: 'dark orange',
        5: 'white',
        6: 'deep pink',
        7: 'light sea green',
        8: 'silver',
        9: 'ivory'
        } # TODO - define colors dictionary

food_color = '' # https://trinket.io/docs/colors

# function to set up the main screen
def set_screen():
    """Sets the main screen."""
    
    global window
    
#TODO - create the window (Screen) and give it; title, background, width-height. And set the tracer.
    window = turtle.Screen() 
    window.title('Snake Game Project')
    window.bgcolor('blue')
    window.setup(width=WIDTH, height=HEIGHT)
    window.tracer(0) # False
    turtle.resetscreen()

# function to listen screen events
def listen_events():
    window.listen()
    
    window.onkeypress(set_up_direction, 'Up') #TODO - listen Up, Down, Left and Right key press events
    window.onkeypress(set_down_direction, 'Down')
    window.onkeypress(set_left_direction, 'Left')
    window.onkeypress(set_right_direction, 'Right')

# keyboard functions
def set_up_direction(): #TODO - complete the functions
    global direction #TODO - set the global direction to up 
        
    if direction != 'down':
        direction = 'up'
        
def set_down_direction():
    global direction
    
    if direction != 'up':
        direction = 'down'
        
def set_left_direction():
    global direction
    
    if direction != 'right':
        direction = 'left'
        
def set_right_direction():
    global direction
    
    if direction != 'left':
        direction = 'right'

def create_head(is_initial=True): # create the head
    """Creates the snake head."""
    
    global head, snake
    
    head = turtle.Turtle() #TODO - create the head turtle, give it a shape and a color.
    head.shape(shapes[0])  #20 x 20
    head.speed(0)
    head.penup()
    
    if is_initial: #TODO - set the position for the head
        head.goto(0, 100)
        
    snake.append(head) #TODO - append the head into snake list

# create the score
def create_score():
    
    global pen    
    # create the pen turtle   
    pen = turtle.Turtle()  #TODO - create the pen turtle and place it on screen
    pen.penup()
    pen.hideturtle()    
    pen.goto(0, Y_RANGE - 2 * TURTLE_SIZE)
    pen.color('black')
    
    # initialize the score
    update_score(0) #TODO - call the update_score function to initialize the pen

# update the score
def update_score(score_increment, is_reset=False):   
    global score, high_score     
    
    if is_reset: #TODO - update the global score and high_score variables, based on is_reset
        score = 0
    
    else:
        score += score_increment
            
        if score > high_score: #TODO - check if the score is greater than the high_score
            high_score = score
            
    pen.clear()  #TODO - clear the pen
    pen.write("Score: {0} |  High Score: {1}".format(score, high_score),
              align='center', font=('Arial', 16, 'normal'))
    
# function to update screen
def update_screen():    
    while window._RUNNING:

        # side collisions
        check_border_collisions() #TODO - call check_border_collisions function
        
        # body collisions
        check_body_collisions() #TODO - call check_body_collisions function
            
        # move the head
        move() #TODO - call move function
        
        # delay
        delay(delay_time) #TODO - call delay function with global delay_time
        
        # create the food
        add_food() #TODO - call add_food function
        
        # eat the food
        eat_food() #TODO - call eat_food function
        
        window.update() # get rid of upate error

# function for border collisions
def check_border_collisions():
    
    # if the head position (x, y) is out the ranges (X_RANGE, Y_RANGE) -> we collide
    
    x = head.xcor() #TODO - get x and y coordinates of the head turtle
    y = head.ycor()
    
    if x <= -X_RANGE or x >= X_RANGE or y <= -Y_RANGE or y >= Y_RANGE: #TODO decide the collision :
        
        # set direction
        global direction #TODO - set the global direction variable to 'stop'
        direction = 'stop'
    
        # reset screen after 1 second
        delay(1) #TODO - call delay function with 1 seconds
                 
        reset() #TODO - call reset function

# Body collisions
def check_body_collisions():
    
    # if the distance betwwen the head and any of the segments is less than the TURTLE_SIZE, then this means we collide.

    #for ...#TODO - get all turtles and indices for the snake...:
    for i, t in enumerate(snake):
                
        # exclude head, TODO - exclude head index:
        if i > 0: #if ...#TODO - get the distance between the head and the current turtle in the loop... < TURTLE_SIZE - 1:
            if head.distance(t) < TURTLE_SIZE - 1:
                
                # set direction
                global direction
                direction = 'stop' #TODO - set the global direction variable to 'stop'

                # reset screen after 1 second
                delay(1) #TODO - call delay function with 1 seconds
                            
                reset() #TODO - call reset function
               
# reset screen funtion
def reset():
    for t in snake: # hide the segments of snake
        t.goto(40000, 4000)
    
    snake.clear() # clear the snake
    
    # create a new head
    create_head(is_initial=False) #TODO - call create_head function with is_initial parameter being False

    # reset the score
    update_score(0, is_reset=True) #TODO - call update_score function with score_increment as 0 and is_reset as True

# move function
def move():
    if window._RUNNING:     
        if direction != 'stop': # move only if the direction is not stop
            
            # move the segments
            move_segments() #TODO - call move_segments function

            # move the head
            move_head() #TODO - call move_head function

# function to move the head
def move_head():    
    # get current coordinate
    x = head.xcor() #TODO - get x and y coordinates of the head turtle
    y = head.ycor()

    if direction == 'up':
        head.sety(y + TURTLE_SIZE)
    elif direction == 'down':
        #TODO - set the y coordinate of the head appriopliately -> remember the turtle moves TURTLE_SIZE pixels
        head.sety(y - TURTLE_SIZE)
        
    elif direction == 'left':
        #TODO - set the x coordinate of the head appriopliately -> remember the turtle moves TURTLE_SIZE pixels
        head.setx(x - TURTLE_SIZE)
    elif direction == 'right':
        #TODO - set the x coordinate of the head appriopliately -> remember the turtle moves TURTLE_SIZE pixels
        head.setx(x + TURTLE_SIZE)

# function to move segments
def move_segments():
    
    # move each segment in reverse order -> from last segment
    # move each segment into the position of the previous one
    # ignore the head
    # start from the last one -> len(snake)-1
    # up to head -> 0
    # backwards -> -1
    
    for i in range(len(snake)-1, 0, -1):
        x = snake[i-1].xcor()  #TODO - get the x and y coordinate of the previous segment
        y = snake[i-1].ycor()
            
        snake[i].goto(x, y)  #TODO - place the current turtle in the loop at x and y

# delay function
def delay(duration):
    time.sleep(duration)

# create food
def add_food():
    if window._RUNNING:
        global food
        # create a turtle -> single -> Singleton Pattern
        if food == None: #TODO - create food for the turtle and give it a random shape
            food = turtle.Turtle()
            food.shape(get_shape())
            food.shapesize(0.5, 0.5)
            food.speed(0)
            food.penup()
            
            # color
            food.color(get_color()) #TODO - give food turtle a random color
            
            # move the food
            move_food(food) #TODO - call move_food function with the food turtle

# function to move the food
def move_food(food):
    
    # x coordinate
    x = random.randint(-X_RANGE, X_RANGE) #x = #TODO - get a random integer between -X_RANGE and X_RANGE
    
    # y coordinate
    y = random.randint(-Y_RANGE, Y_RANGE) #y = TODO - get a random integer between -Y_RANGE and (Y_RANGE - 2 * TURTLE_SIZE)
    
    food.goto(x, y) # replace the food
    
# function to eat the food
def eat_food():    
    if head.distance(food) < TURTLE_SIZE - 1: # check the distance between the head and the food
        
        # move the fodd
        move_food(food) #TODO - call the move_food function with the food
        
        # change the food shape
        food.shape(get_shape()) #TODO - change the food shape to a random one
        
        # create a segment for the snake
        create_segment() #TODO - call create_segment function
        
        # change the food color
        food.color(get_color()) #TODO - give food turtle a random color     
        
        # update score
        update_score(10) #TODO - call update_score function with 10 as increment

# function to create segment
def create_segment():
    """Creates a new segment for snake."""
    
    global snake    
    # create a segment
    segment = turtle.Turtle() #TODO - create the segment turtle with appropiate shape
    segment.shape(shapes[1])
    segment.speed(0)
            
    segment.color(food_color) #TODO - set the color of the segment turtle to global food_color
    segment.penup()
    
    # position the segment
    x, y = get_last_segment_position() #TODO - call get_last_segment_position function
    segment.goto(x, y)
    
    # add this segment into snake list
    snake.append(segment)   #TODO - append the segment to global snake list 

# last segment position
def get_last_segment_position():    
    # last element -> snake[-1]
    x = snake[-1].xcor() #TODO - get the x and y coordinates of the last segment in the snake
    y = snake[-1].ycor()
    
    # direction, if direction is up -> same x, y is TURTLE_SIZE less
    if direction == 'up':
        y = y - TURTLE_SIZE
    
    # if direction is up -> same x, y is TURTLE_SIZE more
    elif direction == 'down':
        y = y + TURTLE_SIZE #TODO - assign the new y value
        
    # if direction is right -> same y, x is TURTLE_SIZE less
    elif direction == 'right':
        x = x - TURTLE_SIZE #TODO - assign the new x value
        
    # if direction is left -> same y, x is TURTLE_SIZE more
    elif direction == 'left':
        x = x + TURTLE_SIZE #TODO - assign the new x value    
    return(x, y) #TODO - return a tuple of x and y

# get a random shape
def get_shape():    
    index = random.randint(0, len(shapes)-1)    
    return shapes[index]

# get a random color
def get_color():    
    global food_color    
    index = random.randint(0, len(colors)-1) #TODO - get a random integer between 0 and the length of colors -1
    color = colors[index]    
    food_color = color    
    return color

set_screen()

listen_events() # listen keyboard events

create_head()

create_score()

update_screen()

turtle.mainloop() # the last line