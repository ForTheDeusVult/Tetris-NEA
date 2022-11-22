import pygame, random
from GLOBAL_VARIABLES import *
from scoring import *
from seven_bag import *

#0  1  2  3
#4  5  6  7
#8  9  10 11
#12 13 14 15

#AAAAAAAAAAAAAAAAAAAAA
shapes = [
    [[4, 5, 6, 7], [2, 6, 10, 14], [8, 9, 10, 11], [1, 5, 9, 13]], #I
    [[0, 4, 5, 6], [1, 2, 5, 9], [4, 5, 6, 10], [1, 5, 8, 9]], #J
    [[2, 4, 5, 6], [1, 5, 9, 10], [4, 5, 6, 8], [0, 4, 8, 9]], #L
    [[1, 4, 5, 6], [1, 5, 6, 9], [4, 5, 6, 9], [1, 4, 5, 9]], # T
    [[0, 1, 5, 6], [1, 5, 6, 10], [4, 5, 9, 10], [0, 4, 5, 9]], #Z
    [[1, 2, 4, 5], [1, 5, 6, 10], [5, 6, 8 ,9], [0, 4, 5, 9]], #S
    [[1, 2, 5, 6]] #O
]

shape_colors = [aqua, navy, orange, yellow, green, purple, red]

#fuck you
Seven_bag = bag()

#really fucking long class for some reason
class block:
    x = 0
    y = 0
    n = 0 
    
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.type = n
        self.color = n
        self.rotation = 0

    def image(self):
        global shapes
        return shapes[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(shapes[self.type])

class Tetris:
    level = 1
    lines = 0
    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    zoom = 20
    x = 100
    y = 60
    block = None
    next_block = None
    stored_block = None
    valid = 0
    count = -1


    def __init__(self, height, width):
        self.height = height
        self.width = width
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def create_new_block(self):
        Seven_bag.__shuffle__
        self.count += 1
        self.block = block(3, 0, Seven_bag._7bag[self.count])

    def create_next_block(self):
        self.count += 1
        if self.count == 7:
            Seven_bag.__shuffle__
            self.count = 0
        self.next_block=block(3,0, Seven_bag._7bag[self.count])

    def load_next_block(self):
        self.block = self.next_block

    #literally god lmao
    def intersect(self):
        intersection = False
        for i in range (4):
            for j in range(4):
                if (i * 4) + j in self.block.image():
                    if i + self.block.y > self.height -1 or j + self.block.x > self.width - 1 or self.field[i + self.block.y][j + self.block.x] > 0:
                        intersection = True
        return intersection

    #how the FUCK does this work
    def clear(self, level):
        lines = 0
        for i in range(1, self.height):
            clear = True
            for j in range(self.width):
                if self.field[i][j] == 0:
                    clear = False
                if clear:
                    lines += 1
                    for k in range(i, 1, -1):
                        for j in range(self.width):
                            self.field[k][j] = self.field[k-1][j]
        self.score += score(level, lines)
        self.lines += lines
        self.increase_level(lines, level)
    
    def increase_level(self, lines, level):
        if self.lines > 10:
            self.level += 1
            lines -= 10

    #engineer? yeah, i'm engiNEARING MY FUCKING LIMIT
    def draw_next_block(self, screen):

        font = Font(30, False)
        label = font.render("Next Shape", 1, white)

        sx = topLeft_x + gameWidth + 50
        sy = topLeft_y + gameHeight/2 - 50
        format = self.next_block.image()
        for i in range(0, 4):
            for j in range(0, 4):
                p = i*4 + j
                if p in self.next_block.image():
                    pygame.draw.rect(screen, shape_colors[self.next_block.color],(sx + j*30, sy + i*30, 30, 30), 0)

    def draw_stored_black(self, screen):

        font = Font(30, False)
        label = font.render("Stored Shape", 1, white)

        sx = topLeft_x + gameWidth + 50
        sy = topLeft_y + gameHeight/2 - 150
        if self.stored_block is not None:
            format = self.stored_block.image()
            for i in range(0,4):
                for j in range(0,4):
                    p = i*4 + j
                    if p in self.stored_block.image():
                        pygame.draw.rect(screen, shape_colors[self.stored_block.color],(sx + j*30, sy + i*30, 30, 30), 0)

    def soft_drop(self, game, level):
        self.block.y += 1
        if self.intersect():
            self.block.y-= 1
            self.freeze(game, level)

    def hard_drop(self, game, level):
        while not self.intersect():
            self.block.y += 1
        self.block.y -= 1
        self.freeze(game, level)

    def store_block(self, valid):
        valid += 1
        if valid < 2:
            if self.stored_block is None:
                self.stored_block = self.block
                self.block = self.next_block
            else:
                temp = self.stored_block
                self.stored_block = self.block
                self.block = self.stored_block
        else:
            return

    def freeze(self, game, level):
        for i in range(0, 4):
            for j in range(0, 4):
                if (i * 4) + j in self.block.image():
                    self.field[i + self.block.y][j + self.block.x] = self.block.color
        self.clear(level)
        self.valid = 0
        block = game.next_block
        self.check_over()
        self.load_next_block()

    def check_over(self):
        if self.intersect():
            self.state = "gameover"


    def move(self, dx):
        old_x = self.block.x
        self.block.x += dx
        if self.intersect():
            self.block.x = old_x

    def rotate(self):
        old_rotation = self.block.rotation
        self.block.rotate()
        if self.intersect():
            self.block.rotation = old_rotation

def DAS(input, game):
    key_delay = 100
    key_interval = 50
    pygame.key.set_repeat(key_delay, key_interval)

    if input == "down":
        game.soft_drop(game, game.level)
    if input == "left":
        game.move(-1)
    if input == "right":
        game.move(1)



def start_game():
    done = False
    clock = pygame.time.Clock()
    fps = 30
    game = Tetris(20, 10)
    counter = 0
    valid = 0

    
    while not done:
        if game.block is None:
             game.create_new_block()
        if game.next_block is None:
            game.create_next_block()
        counter += 1
        if counter > 10000:
            counter = 1

        if counter % (fps // game.level // 2) == 0:
            if game.state == "start":
                game.soft_drop(game, game.level)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.rotate()
                if event.key == pygame.K_DOWN:
                    DAS("down", game)
                if event.key == pygame.K_LEFT:
                    DAS("left", game)
                if event.key == pygame.K_RIGHT:
                    DAS("right", game)
                if event.key == pygame.K_SPACE:
                    game.hard_drop(game, game.level)
                if event.key == pygame.K_k:
                    game.store_block(valid)
                if event.key == pygame.K_ESCAPE:
                    game.__init__(20, 10)
        
        screen.fill(black)
        
        for i in range(game.height):
            for j in range(game.width):
                pygame.draw.rect(screen, white, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:
                    pygame.draw.rect(screen, shape_colors[game.field[i][j]], [game.x + game.zoom * j +1, game.y + game.zoom * i + 1, game.zoom -2, game.zoom -1])


        if game.block is not None:
            for i in range(0, 4):
                for j in range(0, 4):
                    p = i * 4 + j
                    if p in game.block.image():
                        pygame.draw.rect(screen, shape_colors[game.block.color], [game.x + game.zoom * (j + game.block.x) + 1, game.y + game.zoom * (i + game.block.y) + 1, game.zoom - 2, game.zoom - 2])
    
        score_font = Font(40, False)
        label = font.render("Score: " + str(game.score), True, white)

        screen.blit(label, (300, 0))

        game_over_font = Font(25, False)
        game_over_label1 = font.render("Game Over!", True, white)
        game_over_label2 = font.render("Press ESC", True, white)

        if game.state == "gameover":
            screen.blit(game_over_label1, (300, 200))
            screen.blit(game_over_label2, (300,200))

        game.draw_next_block(screen)

        pygame.display.flip()
        clock.tick(fps)

pygame.font.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris - Normal Mode")

run = True
while run:
    screen.fill(black)
    font = Font(30, True)
    label = font.render("Press any key to start!", False, white)

    screen.blit(label, (10, 300))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            start_game()
pygame.quit()
