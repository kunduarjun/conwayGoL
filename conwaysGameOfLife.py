# Conway's Game of Life.
# This program was created by Al Sweigart, who is the author of "Automating the Boring Stuff with Python."
# Al Sweigart demonstrated how to program this simulation through a video on his YouTube channel. 
# I am simply following along to his YouTube video, as I am looking to populate my GitHub with more reposiitories.

# Rules of the game:
# 1) Living cells with 2 or 3 neighbours stay alive.
# 2) Dead cells with 3 living neighbours become alive again.
# 3) All other cells become or stay dead. 

# Press Ctrl-C to stop the simulation. 

import copy, random, sys, time

# Set up some constants within the program
WIDTH = 79 # Width of the cell grid.
HEIGHT = 20 # Height of the cell grid. 
ALIVE = "O" # This character will represent an alive cell.
DEAD = " " # Empty space character will represent a dead cell. 

# nextCells and cells are what we will call the dictionaries containing the information stored within our grid
# Keys will be (x,y) coordinate tuples. Values will either be the ALIVE character or the DEAD character.

nextCells = {}

# Put random ALIVE and DEAD cells into nextCells to start
for x in range(WIDTH): # Covers columns of the grid
    for y in range(HEIGHT): # Covers Rows of the grid
        # 50/50 chance of a cell being dead or alive.
        if random.randint(0,1) == 0:
            nextCells[(x,y)] = ALIVE # Add a living cell into the nextCells dictionary.
        else:
            nextCells[(x,y)] = DEAD # Add a dead cell into the nextCells dictionary.

while True: # Program loop. Every iteration is a simulation step.
    print("\n" * 50) # This will just clear the screen displayed by printing newline characters. 

    # Cells of the "next step" become the cells of the "curent step".
    cells = copy.deepcopy(nextCells)

    # Print the contents of the grid.
    for y in range(HEIGHT): # Loop the rows from top to bottom.
        for x in range(WIDTH): # Loop the columns from left to right.
            # Set end = '' to avoid printing a newline before the end of each row. 
            print(cells[(x,y)], end = '') # Print the value of the specified coordinate.
        print() # Print a newline at the end of each row. 
    print("Press Ctrl-C to exit the simulation.")

    # Determine the cells contained within the next step, based on the cells containted within this step.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neighbouring coordinates for (x,y).
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y  - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # Count the number of living neighbours.
            numNeighbours = 0
            if cells[(left, above)] ==  ALIVE:
                numNeighbours += 1 # Top-left neighbour is alive.
            if cells[(x, above)] == ALIVE:
                numNeighbours += 1 # Top neighbour is alive.
            if cells[(right, above)] == ALIVE:
                numNeighbours += 1 # Top-right neighbour is alive.
            if cells[(left, y)] == ALIVE:
                numNeighbours += 1 # Left neighbour is alive. 
            if cells[(right, y)] == ALIVE:
                numNeighbours += 1 # Right neighbour is alive.
            if cells[(left, below)] == ALIVE:
                numNeighbours += 1 # Bottom-left neighbour is alive.
            if cells[(x, below)] == ALIVE:
                numNeighbours += 1 # Bottom neighbour is alive.
            if cells[(right, below)] == ALIVE:
                numNeighbours += 1 # Bottom-right neighbour is alive. 
            
            # Set cells based on Conway's Game of Life rules
            if cells[(x,y)] == ALIVE and (numNeighbours == 2 or numNeighbours == 3):
                # Living cells remain living if they have 2 or 3 alive neighbours.
                nextCells[(x,y)] = ALIVE
            elif cells[(x,y)] == DEAD and numNeighbours == 3:
                # Dead cells with 3 living neighbours come back to life.
                nextCells[(x,y)] = ALIVE
            else:
                # Otherwise, cells will become or remain dead.
                nextCells[(x,y)] = DEAD
            
    try:
        time.sleep(2) # Add a 2 second pause to reduce flickering and strain on eyes.
    except KeyboardInterrupt:
        print()
        print("Conway's Game of Life")
        print("By Al Sweigart, copied by Arjun Kundu")
        sys.exit() # When Ctrl-C is pressed, end the program.
