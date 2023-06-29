# This is a program created by Al Sweigart, who is the author of "Automating the Boring Stuff with Python."
# Al Sweigart demonstrated how to program this game through his YouTube channel. 
# I am simply following along to his YouTube video, as I am looking to populate my GitHub with more reposiitories.
# I will add comments onto this program, in order to demonstrate that I understand what was discussed in the video.
# This will also demonstrate that I understand the requirements to program this game. 

# Rules of the game:
# 1) Living cells with 2 or 3 neighbours stay alive.
# 2) Dead cells with 3 living neighbours become alive again.
# 3) All other cells become or stay dead. 

# Press Ctrl-C to stop the simulation. 

import copy, random, sys, time

# Set up some constants within the program
WIDTH = 45 # Width of the cell grid.
HEIGHT = 25 # Height of the cell grid. 

