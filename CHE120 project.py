from random import choice
from turtle import *

from freegames import floor, vector

prev_tile = 0

state = {'score': 0}
path = Turtle(visible=False)
path_second_player = Turtle(visible=False) #second player
writer = Turtle(visible=False)
writer_second_player = Turtle(visible=False)#second player
aim = vector(5, 0) 
aim_second_player = vector(5, 0) #second player
pacman = vector(-40, -80)
pacman_second_player = vector(-20, -80) #second player
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
    [vector(0, -40), vector(-5, 5)],
]
# fmt: off
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 4, 1, 1, 1, 1, 0, 10, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 3, 0, 0, 0, 0,
    0, 1, 3, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 12, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    9, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 4, 1, 1, 1, 8,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 5, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 3, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 13, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 4, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
# fmt: on


def square(x, y):
    """Draw square using path at (x, y)."""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):
    """Return True if point is valid in tiles."""
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    """Draw world using path."""
    bgcolor('#A8E6CF') #KT: more matching theme to cute garden
    path.color('#F5F5DC') #KT: more matching theme to cute garden

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

            elif tile == 3:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(10, 'purple')
                
            elif tile == 4:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(15, 'green')
                
            elif tile == 5:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(20, 'orange')
                
            elif tile == 8 or tile == 9 or tile == 10 or tile == 11:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(20, 'white')
                path.dot(17, 'black')
                
            elif tile == 12:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(20, 'black')
                
            elif tile == 13:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(20, 'white')

def move():
    """Move pacman and all ghosts."""
    writer.undo()
    writer.write(state['score'])

    clear()

    global prev_tile
    global prev_tile_second_player

    prev_index = offset(pacman)
    prev_tile = tiles[prev_index]
    
    prev_index_second_player = offset(pacman_second_player)
    prev_tile_second_player = tiles[prev_index_second_player]

    if valid(pacman + aim):
        pacman.move(aim)
        
    if valid(pacman_second_player + aim_second_player): #second player
        pacman_second_player.move(aim_second_player) #second player
        

    index = offset(pacman)
    index_second_player = offset(pacman_second_player) #second player
    current_tile = tiles[index]
    current_tile_second_player = tiles[index_second_player]

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    if tiles[index] == 3:
        tiles[index] = 2
        state['score'] += 5
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    if tiles[index] == 4:
        tiles[index] = 2
        state['score'] += 10
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)
        
    if tiles[index] == 5:
        tiles[index] = 2 
        state['score'] += 50
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)
        
    if current_tile in (8, 9) and prev_tile not in (8, 9):
            index = offset(pacman)
            portal()
            
    if tiles[index_second_player] == 1:#second player
        tiles[index_second_player] = 2#second player
        state['score'] += 1#second player
        x = (index_second_player % 20) * 20 - 200#second player
        y = 180 - (index_second_player // 20) * 20#second player
        square(x, y)#second player

    if tiles[index_second_player] == 3:#second player
        tiles[index_second_player] = 2#second player
        state['score'] += 5#second player
        x = (index_second_player % 20) * 20 - 200#second player
        y = 180 - (index_second_player // 20) * 20#second player
        square(x, y)#second player

    if tiles[index_second_player] == 4:#second player
        tiles[index_second_player] = 2#second player
        state['score'] += 10#second player
        x = (index_second_player % 20) * 20 - 200#second player
        y = 180 - (index_second_player // 20) * 20#second player
        square(x, y)#second player
        
    if tiles[index_second_player] == 5:#second player
        tiles[index_second_player] = 2#second player
        state['score'] += 50#second player
        x = (index_second_player % 20) * 20 - 200#second player
        y = 180 - (index_second_player // 20) * 20#second player
        square(x, y)#second player

        
    if current_tile_second_player in (8, 9, 10, 11, 12) and prev_tile_second_player not in (8, 9, 10, 11):
        index_second_player = offset(pacman_second_player)
        portal_second_player()
    
    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')
    
    up() #second player
    goto(pacman_second_player.x + 10, pacman_second_player.y + 10) #second player
    dot(20, 'blue') #second player

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
                vector(-5, 5),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, '#9B1B30') #KT: changed the colour to match the cutsy garden theme
#KT: i muted this part im trying to chnage the shape of the main charatcer but im having toruble making sure the code removed there its already been. leave this commented out part here in case we have to settle for the dot in the end.
        up()
        goto(pacman.x, pacman.y)  #KT: to move our character arcoss the x and y asis
        path.color('pink')  #KT: changed the colour of the character from yellow to pink
        for _ in range(5):  # Draw a star
            path.forward(20)
            path.right(144)
        path.end_fill()


    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            game_over()
            return None
        
    for point, course in ghosts: #second player
        if abs(pacman_second_player - point) < 20: #second player
            game_over()
            return None #second player

    if state['score'] <= 50:
        ontimer(move, 150)
    elif state['score'] <= 100 and state['score'] > 50:
        ontimer(move, 100)
    elif state['score'] <= 200 and state['score'] > 100:
        ontimer(move, 50)  
    else:
        ontimer(move, 25)

def change(x, y):
    """Change pacman aim if valid."""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y
        
def change_second_player(x, y): #second player
    if valid(pacman_second_player + vector(x, y)): #second player
        aim_second_player.x = x #second player
        aim_second_player.y = y #second player


def portal():
    """ Transports the first pacman from one point to another"""
    index = offset(pacman)
    if tiles[index] == 8:
        for i in range(len(tiles)):
            if tiles[i] == 9:
                x = (i % 20) * 20 -200
                y = 180 - (i // 20) * 20
                pacman.x = x
                pacman.y =y
                return
            
    elif tiles[index] == 9:
        for i in range(len(tiles)):
            if tiles[i] == 8:
                x = (i % 20) * 20 -200
                y = 180 - (i // 20) * 20
                pacman.x = x
                pacman.y =y
                return
            
    elif tiles[index] == 10:
        for i in range(len(tiles)):
            if tiles[i] == 11:
                x = (i % 20) * 20 -200
                y = 180 - (i // 20) * 20
                pacman.x = x
                pacman.y =y
                return
     
    elif tiles[index] == 11:
        for i in range(len(tiles)):
            if tiles[i] == 10:
                x = (i % 20) * 20 -200
                y = 180 - (i // 20) * 20
                pacman.x = x
                pacman.y =y
                return
            
    elif tiles[index] == 12:
         for i in range(len(tiles)):
             if tiles[i] == 13:
                 x = (i % 20) * 20 -200
                 y = 180 - (i // 20) * 20
                 pacman.x = x
                 pacman.y =y
                 return

            
def portal_second_player():
    """ Transports the second pacman from one point to another"""
    index_second_player = offset(pacman_second_player)
    if tiles[index_second_player] == 8:
        for i in range(len(tiles)):
            if tiles[i] == 9:
                x = (i % 20) * 20 -200
                y = 180 - (i // 20) * 20
                pacman_second_player.x = x
                pacman_second_player.y =y
                return
            
    elif tiles[index_second_player] == 9:
        for i in range(len(tiles)):
            if tiles[i] == 8:
                x = (i % 20) * 20 -200
                y = 180 - (i // 20) * 20
                pacman_second_player.x = x
                pacman_second_player.y =y
                return
            
    elif tiles[index_second_player] == 10:
        for i in range(len(tiles)):
            if tiles[i] == 11:
                x = (i % 20) * 20 -200
                y = 180 - (i // 20) * 20
                pacman_second_player.x = x
                pacman_second_player.y =y
                return
            
    elif tiles[index_second_player] == 11:
        for i in range(len(tiles)):
            if tiles[i] == 10:
                x = (i % 20) * 20 -200
                y = 180 - (i // 20) * 20
                pacman_second_player.x = x
                pacman_second_player.y =y
                return
            
    elif tiles[index_second_player] == 12:
         for i in range(len(tiles)):
             if tiles[i] == 13:
                 x = (i % 20) * 20 -200
                 y = 180 - (i // 20) * 20
                 pacman_second_player.x = x
                 pacman_second_player.y =y
                 return

def game_over():
    """"Checks how the game ended, and prints the appropriate response """
    for point, course in ghosts:
        if 1 not in tiles:
            print('Congrats! You won :)')
        elif abs(pacman - point) < 20 or abs(pacman_second_player - point) < 20:
            print('Too bad! You lost :(')
    print('Press r for instructions to play again or e for how to end the session.')

def play_again():
    """Gives instructions on playing again and closes the graphics window for a smooth transition."""
    print('Click on the code and run it again!')
    bye()
    
def end_session():
    """Gives instructions on how to exit the game without issues."""
    print('Close the graphics window and console')
    done()
    bye()

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
onkey(lambda: change_second_player(5, 0), 'd') #second player
onkey(lambda: change_second_player(-5, 0), 'a') #second player
onkey(lambda: change_second_player(0, 5), 'w') #second player
onkey(lambda: change_second_player(0, -5), 's') #second player
onkey(lambda: play_again(), 'r')
onkey(lambda: done(), 'e')
world()
move()
done()
