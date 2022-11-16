#SCORE SYSTEM
#Based on the Original Tetris Scoring System (NES/GAMEBOY/SNES)

def score(level, lines):

    score = 0

    if lines == 1:
        score = (40*level)
    elif lines == 2:
        score = (100*level)
    elif lines == 3:
        score = (300*level)
    elif lines == 4:
        score = (400*level)
    
    return score

