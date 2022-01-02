import numpy
import pygame
import math


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                        (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


start = (4, 3)
end = (8, 5)
start1 = (4, 0)
end1 = (8, 7)
start2 = (3, 1)
end2 = (8, 6)


def pathsolver():
    a = 10
    maze = []
    for i in range(a):
        row = []
        for j in range(a):
            row.append(0)
        maze.append(row)

    path = astar(maze, start, end)
    a1=path
    print(path)

    path1 = astar(maze, start1, end1)
    a2=path1
    print(path1)

    path2 = astar(maze, start2, end2)
    a3=path2
    print(path2)
    search = True
    current = 0
    carpisma = 0

    while search:
        print("Arama başladı...")
        while current < min(len(path), len(path1)):
            for i in range(current, min(len(path), len(path1))):
                print("Arama sürüyor....")
                if path[i] == path1[i]:
                    a, b = path[i]
                    maze[a][b] = 1
                    path1 = astar(maze, start1, end1)
                    print("Çarpışma algılandı....")

                    current = i+1
                    carpisma += 1
                    break
                if i == min(len(path), len(path1))-1 and path[i] != path1[i]:
                    print("Arama tamam!")
                    current = min(len(path), len(path1))
        current = 0
        while current < min(len(path1), len(path2)):
            for i in range(current, min(len(path1), len(path2))):
                print("Arama sürüyor....")
                if path1[i] == path2[i]:
                    a, b = path2[i]
                    maze[a][b] = 1
                    path2 = astar(maze, start2, end2)
                    print("Çarpışma algılandı....")



                    current = i+1
                    carpisma += 1
                    break
                if i == min(len(path1), len(path2))-1 and path1[i] != path2[i]:
                    print("Arama tamam!")
                    current = min(len(path1), len(path2))
        current = 0
        while current < min(len(path), len(path2)):
            for i in range(current, min(len(path), len(path2))):
                print("Arama sürüyor....")
                if path[i] == path2[i]:
                    a, b = path2[i]
                    maze[a][b] = 1
                    path2 = astar(maze, start2, end2)
                    print("Çarpışma algılandı....")

                    current = i+1
                    carpisma += 1
                    break
                if i == min(len(path), len(path2))-1 and path[i] != path2[i]:
                    print("Arama tamam!")
                    current = min(len(path), len(path2))
        search = False

    print(path)
    print(path1)
    print(path2)
    print("Toplamda " + carpisma.__str__() + " çarpışma engellendi...")
    return path,path1,path2,a1,a2,a3

# Define some colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the height and width of the screen
size = [700, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Instruction Screen")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# The paths of each AGV
xy1, xy2, xy3, a1, a2, a3 = pathsolver()




#to show total time on screen
timeForAgv1 = len(xy1)
timeForAgv2 = len(xy2)
timeForAgv3 = len(xy3)
###



loop = 0


# This is a font we use to draw text on the screen (size 30)
font = pygame.font.SysFont("comicsansms", 25)

display_instructions = True
instruction_page = 1

# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 3:
                display_instructions = False

    # Set the screen background
    screen.fill(BLACK)

    if instruction_page == 1:
        # Draw instructions, page 1

        text = font.render("Hello AI", True, WHITE)
        screen.blit(text, [10, 10])

        text = font.render("Click to start...", True, WHITE)
        screen.blit(text, [10, 40])

    if instruction_page == 2:
        # Draw instructions, page 2
        text = font.render("This is a simulation of Conflict-Free Route Planning AI", True, WHITE)
        screen.blit(text, [10, 10])

        text = font.render("Click to start...", True, WHITE)
        screen.blit(text, [10, 40])

    # Limit to 60 frames per second
    clock.tick(60)

    # Updating screen
    pygame.display.flip()

def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=10):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dl = dash_length

    if (x1 == x2):
        ycoords = [y for y in range(y1, y2, dl if y1 < y2 else -dl)]
        xcoords = [x1] * len(ycoords)
    elif (y1 == y2):
        xcoords = [x for x in range(x1, x2, dl if x1 < x2 else -dl)]
        ycoords = [y1] * len(xcoords)
    else:
        a = abs(x2 - x1)
        b = abs(y2 - y1)
        c = round(math.sqrt(a**2 + b**2))
        dx = dl * a / c
        dy = dl * b / c

        xcoords = [x for x in numpy.arange(x1, x2, dx if x1 < x2 else -dx)]
        ycoords = [y for y in numpy.arange(y1, y2, dy if y1 < y2 else -dy)]

    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x1, y1), (x2, y2) in zip(next_coords, last_coords):
        start = (round(x1), round(y1))
        end = (round(x2), round(y2))
        pygame.draw.line(surf, color, start, end, width)

def PrintPath(xy1,xy2,xy3 , withDash=False):
    n = 0
    k = 0
    m = 0
    a = xy1[n ]
    b = xy2[k ]
    c = xy3[m ]
    rect_x = 96 + a[0] * 50
    rect_y = 96 + a[1] * 50
    rect_x2 = 96 + b[0] * 50
    rect_y2 = 96 + b[1] * 50
    rect_x3 = 96 + c[0] * 50
    rect_y3 = 96 + c[1] * 50
    rect_xx = rect_x
    rect_yy = rect_y
    rect_x2x = rect_x2
    rect_y2y = rect_y2
    rect_x3x = rect_x3
    rect_y3y = rect_y3

    i = 0
    while (i < loop):
        i += 1
        if(withDash):
            draw_dashed_line(screen, GREEN, (rect_x, rect_y), (rect_xx, rect_yy), 10, 3)
            draw_dashed_line(screen, RED, (rect_x2, rect_y2), (rect_x2x, rect_y2y), 10, 5)
            draw_dashed_line(screen, BLUE, (rect_x3, rect_y3), (rect_x3x, rect_y3y), 10, 7)
        else:
            pygame.draw.line(screen, GREEN, (rect_x, rect_y), (rect_xx, rect_yy), 10)
            pygame.draw.line(screen, RED, (rect_x2, rect_y2), (rect_x2x, rect_y2y), 10)
            pygame.draw.line(screen, BLUE, (rect_x3, rect_y3), (rect_x3x, rect_y3y), 10)

        rect_xx = rect_x
        rect_yy = rect_y
        a = xy1[n ]
        rect_x = 96 + a[0] * 50
        rect_y = 96 + a[1] * 50
        n += 1
        if (n == len(xy1) ):
            n -= 1

        rect_x2x = rect_x2
        rect_y2y = rect_y2
        b = xy2[k ]
        rect_x2 = 96 + b[0] * 50
        rect_y2 = 96 + b[1] * 50
        k += 1
        if (k == len(xy2) ):
            k -= 1

        rect_x3x = rect_x3
        rect_y3y = rect_y3
        c = xy3[m ]
        rect_x3 = 96 + c[0] * 50
        rect_y3 = 96 + c[1] * 50
        m += 1
        if (m == len(xy3) ):
            m -= 1


# -------- Main Program Loop -----------
while not done:
    loop += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Set the screen background
    screen.fill(WHITE)

    # Drawing the path matrix
    for i in range(100, 650, 50):
        pygame.draw.line(screen, BLACK, [i ,100] , [i, 600],5)

    for j in range(100, 650, 50):
        pygame.draw.line(screen, BLACK, [100 ,j] , [600, j],5)

    # Demonstrating the path of each AGV.
    font = pygame.font.SysFont("Arial", 15)
    text = font.render("AGV-1: {}".format(xy1), True, GREEN)
    screen.blit(text, [0, 0])
    text = font.render("AGV-2: {}".format(xy2), True, RED)
    screen.blit(text, [0, 30])
    text = font.render("AGV-3: {}".format(xy3), True, BLUE)
    screen.blit(text, [0, 60])
    #Total time On screen
    a = 10
    maze = []
    for i in range(a):
        row = []
        for j in range(a):
            row.append(0)
        maze.append(row)

    bpath = astar(maze, start, end)
    b_path_len = len(bpath)
    bpath1 = astar(maze, start1, end1)
    b_path_len1 = len(bpath1)
    bpath2 = astar(maze, start2, end2)
    b_path_len2 = len(bpath2)
    timeDispNameStock = font.render("Before Time For", 1, BLACK)
    screen.blit(timeDispNameStock, [0, 90])
    timeDispName = font.render("AGV-1:", 1, GREEN)
    timeDisplay = font.render(str(b_path_len), 1, GREEN)
    screen.blit(timeDisplay, [50, 120])
    screen.blit(timeDispName, [0, 120])

    timeDispName = font.render("AGV-2:", 1, RED)

    timeDisplay = font.render(str(b_path_len1), 1, RED)
    screen.blit(timeDisplay, [50, 150])
    screen.blit(timeDispName, [0, 150])

    timeDispName = font.render("AGV-3:", 1, BLUE)
    timeDisplay = font.render(str(b_path_len2), 1, BLUE)
    screen.blit(timeDisplay, [50, 180])
    screen.blit(timeDispName, [0, 180])

    timeDispNameStock = font.render("After total Time ", 1, BLACK)
    screen.blit(timeDispNameStock, [0, 210])

    timeDispName = font.render("AGV-1:", 1, GREEN)
    timeDisplay = font.render(str(timeForAgv1), 1, GREEN)
    screen.blit(timeDisplay, [50, 240])
    screen.blit(timeDispName, [0, 240])

    timeDispName = font.render("AGV-2:", 1, RED)
    timeDisplay = font.render(str(timeForAgv2), 1, RED)
    screen.blit(timeDisplay, [50, 270])
    screen.blit(timeDispName, [0, 270])

    timeDispName = font.render("AGV-3:", 1, BLUE)
    timeDisplay = font.render(str(timeForAgv3), 1, BLUE)
    screen.blit(timeDisplay, [50, 300])
    screen.blit(timeDispName, [0, 300])

    # Drawing the AGVs
    PrintPath(a1,a2,a3,True)
    PrintPath(xy1,xy2,xy3,False)

    # Method Name
    maFont = pygame.font.SysFont("comicsansms", 25)
    methodName = maFont.render("Alternative Path Method", 1, BLACK)
    screen.blit(methodName, [250, 600])

    # Limit to 1 frames per second
    clock.tick(1)


    # Updating screen
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
