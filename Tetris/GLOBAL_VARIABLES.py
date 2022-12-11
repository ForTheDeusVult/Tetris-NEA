import pygame

#COLORS
aqua = (0, 255, 255)
navy = (0, 0, 255)
orange = (255, 69, 0)
yellow = (255, 255, 0)
purple = (148, 0, 211)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)


#SCREEN DIMENSIONS
width = 700
height = 600
gameWidth = 100  
gameHeight = 400 
blockSize = 20
 
topLeft_x = (width - gameWidth) // 2
topLeft_y = height - gameHeight - 50

def Font(size, bold):
    return(pygame.font.SysFont("Calibri", size, bold))