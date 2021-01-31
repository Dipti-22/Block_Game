# BLOCK GAME

import pygame
import random
import sys


pygame.init()                                                    # initialising pygame 

WIDTH = 1500
HEIGHT = 600

RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,102)
BLACK = (0,0,0)
BACKGROUND_COLOR = (0,255,255)                                       # bg colour black , blue = (50, 153, 213), green = (0, 255, 0), yellow = (255, 255, 102)

player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]                     # setting players position 

enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]              # setting the position of the enemy randomly
enemy_list = [enemy_pos]                                         # for creating lots of enemy blocks 

SPEED = 10


screen = pygame.display.set_mode((WIDTH, HEIGHT))               # for designing screen

game_over = False

score = 0


pygame.display.set_caption('By Dipti Sharma')                    # game's name 

clock = pygame.time.Clock()                                      # to stop screen blinking 

myfont = pygame.font.SysFont("monospace",35)                     

def set_level(score, SPEED):                                     # for changing speed after every interval given 
    if score < 20:
        SPEED = 6
    elif score < 40:
        SPEED = 9
    elif score < 60:
        SPEED = 11
    elif score < 80:
        SPEED = 14
    elif score < 100:
        SPEED = 15
    else:
        SPEED = 20
    return SPEED


def drop_enemies(enemy_list):
    delay = random.random()                                        # it brings randon float / decimal value delay in falling the blocks  
    if len(enemy_list) < 10 and delay < 0.1:                       # to create some sort of distance between falling blocks ** smaller the better 
        x_pos = random.randint(0,WIDTH-enemy_size)                 # making the blocks fall
        y_pos = 0                                                  # starting position of the enemy blocks
        enemy_list.append([x_pos, y_pos])                          # to append the position of block on x, y line 

def draw_enemies(enemy_list):                                      # to draw enemy blocks 
    for enemy_pos in enemy_list:
         pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list, score):                      # repeated fall of enemies blocks  
    for idx, enemy_pos in enumerate(enemy_list):                    # it will countinuosely make the blocks fall 
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:             # this is in order to increase the speed after certain level 
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)
            score += 1                                              # score increasing 
    return score                                                   
            
           
def collision_check(enemy_list, player_pos):                        # checking collision 
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False

def detect_collision(player_pos, enemy_pos):                        # detection of collision 
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True 
    return False 

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size

            player_pos = [x,y]


    screen.fill(BACKGROUND_COLOR)                                     # to prevent red colour of the block

    # update position of the enemy

    # if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
       # enemy_pos[1] += SPEED
    # else:
       # enemy_pos[0] = random.randint(0, WIDTH-enemy_size)           # to make block fall from different positions everytime
       # enemy_pos[1] = 0


    # font = pygame.font.SysFont(None, 35)                            # this is to bring text on the screen 
    #def message_to_screen(msg, color):
    # screen_text = font.render(msg, True, color)
    # game_over.blit(screen_text, [WIDTH/2, HEIGHT/2])


    # while game_close == True:                                       # to get the 
    #   dis.fill(blue)
    #   message("You Lost! Press C-Play Again or Q-Quit", red)


    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)
    SPEED = set_level(score, SPEED)                               # changing speed after a level 
    text = "Score: " + str(score)                                 # increase score on the screen 
    label = myfont.render(text, 1, BLACK)                        # Red = (255,0,0) **** Blue = (0,0,255) *** Black = (0,0,0) *** White =(255,255,255)
    screen.blit(label, (WIDTH-200, HEIGHT-40))                    # showing onto the screen 
    
    if collision_check(enemy_list, player_pos):                   # game over condition
        game_over = True
        break
    
    draw_enemies(enemy_list)
    
    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size ))
    
    clock.tick(30)

    pygame.display.update()