from random import randint, shuffle, choice
import exceptions as exc
import csv
import sys

sys.setrecursionlimit(10000)

# Returns an empty maze of a given size
def make_empty_maze(height, width):
    maze = [[[] for b in range(width)] for a in range(height)]
    return maze

# Converts empty maze to ...
def convert(maze):
    pretty_maze = [[1]*(2*len(maze[0])+1) for a in range(2*len(maze)+1)]
    for y,row in enumerate(maze):
        for x,col in enumerate(row):
            pretty_maze[2*y+1][2*x+1] = 0
            for direction in col:
                pretty_maze[2*y+1+direction[0]][2*x+1+direction[1]] = 0
    #Removing the walls around the maze
    pretty_maze.pop(0)
    pretty_maze.pop(len(pretty_maze)-1)
    for row in pretty_maze:
        row.pop(0)
        row.pop(len(row)-1)
    length = len(pretty_maze)-1
    #Placing the end destination
    pretty_maze[length][length] = 2
    return pretty_maze

def DFS(maze, coords=(0,0)):
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    shuffle(directions)
    for direction in directions:
        new_coords = (coords[0] + direction[0], coords[1] + direction[1])
        if (0 <= new_coords[0] < len(maze)) and (0 <= new_coords[1] < len(maze[0])) and not maze[new_coords[0]][new_coords[1]]:
            maze[coords[0]][coords[1]].append(direction)
            maze[new_coords[0]][new_coords[1]].append((-direction[0], -direction[1]))
            DFS(maze, new_coords)
    return maze

def reset_search(grid):
    visited.clear()
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if(grid[x][y] == 3):
                grid[x][y] = 0
                
# List of coordinates visited when solving the maze
visited = []

####    ALGORITHMS    ###
# Recursive backtracker #
def search(grid, x, y):
    if grid[x][y] == 2:
        #print("Found exit at ({}, {})".format(x, y))
        return True
    elif grid[x][y] == 1:
        return False
    elif grid[x][y] == 3:
        return False
    visited.append(str((y, x)))
    grid[x][y] = 3
    if ((x < (len(grid)-1) and search(grid, x+1, y))
        or (y > 0 and search(grid, x, y-1))
        or (x > 0 and search(grid, x-1, y))
        or (y < len(grid)-1 and search(grid, x, y+1))):
        return True
    return False

# A* Algorithm #
# g = actual length from start cell to current cell
# h = estimated length from current cell to end (without walls)
# f = sum of g and h
class Cell(object):
    def __init__(self, x, y, reachable):
        self.reachable = reachable
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

# heapifies the list with the lowest "f" at the top
# gets the size of the grid
class AStar(object):
    def _init_(self, x, y, reachable, height, width):
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.cells = []
        self.grid_height = height
        self.grid_width = width

# Calculates distance from current to end
def get_h_value(self, cell)
return 10 * (abs(cell.x - cell.end.x) + abs(cell.y - cell.end.y))

# Initializes the grid  - gets start and end coordinate
# Checks where there's walls
def init_grid(grid, x , y):
    for x in range(self.grid_width):
        for y in range(self.grid_height):
            if grid[x][y] = 2
                reachable = False
            else:
                reachable = True
            self. cells.append(Cell (x, y, reachable))
    self.start = self.get_cell(0, 0)
    # For Testing:
    # self.end = self.get_cell(9, 9)
    self.end = self.get_cell(self.grid_height, self.grid_width)
            

################################################################################

def save_maze(filename, maze):
    with open(filename, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(maze)

def read_maze(filename):
    maze = []
    with open(filename, 'r') as f:
        maze = [list(map(int, el)) for el in csv.reader(f, delimiter=',')]
    return maze      

def save_maze_data(filename, maze_data):
    with open(filename, "w", newline='') as f:
        writer = csv.writer(f)
        for row in maze_data:
            for value in maze_data[row]:
                writer.writerow([row, value, maze_data[row][value]])

# Saves to csv with no headers or field names
def save_maze_data2(filename, maze_data):
    with open(filename, "w", newline='') as f:
        writer = csv.writer(f)
        for size in maze_data:
            writer.writerow([size, maze_data[size]['moves'], maze_data[size]['avg_time'], maze_data[size]['min_time'], maze_data[size]['max_time']])

def load_maze_data(filename):
    maze_data = {}
    with open(filename, "r") as f:
        reader = csv.DictReader(f, delimiter=(','))
        for row in reader:
            print(row)
    return maze_data

# Loads the maze data from csv 
def load_maze_data2(filename):
    maze_data = {}
    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=(','))
        for row in reader:
            maze_data[row[0]] = {'moves': row[1], 'avg_time': row[2], 'min_time': row[3], 'max_time': row[4]}
    return maze_data

# Choose an algorithm to use

# # Choose an algorithm to use
# def available_algorithms(choice):
#     solutions = [ {"1": "Recursive"}, {"2": "A*"} ]
#     #solutions = {"1": {"name": "Recursive", "algorithm": search}}
#     if choice not in solutions.keys():
#         raise exc.InvalidInputException("Invalid input - Please try again")
#     else:
#         return solutions[choice-1]

def available_algorithms(choice):
    solutions = {"1": "Recursive", "2": "a*"}
    #solutions = {"1": {"name": "Recursive", "algorithm": search}}
    if choice not in solutions.keys():
        raise exc.InvalidInputException("Invalid input - Please try again")
    else:
        return solutions[choice]

# Returns chosen algorithm to be used
def get_solutions():
    solutions = {"1": "Recursive"}
    return solutions
    
def calc_average(values):
    return sum(values) / len(values)
