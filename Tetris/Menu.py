import pygame, tkinter, sys
from GLOBAL_VARIABLES import *

pygame.init()

screen = pygame.display.set_mode((width + 580, height + 120))
pygame.display.set_caption("Tetris Frenzy")

def main_menu():

    while True:
        screen.fill(black)
        
        mouse_pos = pygame.mouse.get_pos()

        menu_text = Font(100, False).render("TETRIS FRENZY", True, white)
        menu_rect = menu_text.get_rect(center=(640, 100))

        play_button = Button((640, 250), "PLAY", Font(75, False), white, 
