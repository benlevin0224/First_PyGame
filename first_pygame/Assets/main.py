import pygame
from spritesheet import Spritesheet
from character import Character
import json
import os
cwd = os.getcwd()
pygame.display.set_caption("First Game!")

WIDTH, HEIGHT = (900,500)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
WHITE = (255,255,255)
VEL = 5

standing = True
last_update = 0
index = 0
facing_left = False
facing_right = True

walking_spritesheet = Character(cwd + "/sprites/noBKG_KnightRun_strip.png")
walking_len = len(walking_spritesheet.data["frames"])
idle_spritesheet = Character(cwd + "/sprites/noBKG_KnightIdle_strip.png")
idle_len = len(idle_spritesheet.data["frames"])

def draw_window(KnightMove, knight_rec): 
    WIN.fill((WHITE))
    WIN.blit(KnightMove, (knight_rec.x, knight_rec.y))
    pygame.display.update()
    

def knight_movement(keys_pressed, knight_rec):
    global index
    global facing_left
    global facing_right
    global last_update
    global standing
    IMAGE_INTERVAL = 67
    
    #####   UPDATES THE VARIABLES BASED ON KEY PRESS    #####
    if keys_pressed[pygame.K_a] and knight_rec.x - VEL > 0: #LEFT
        standing = False
        knight_rec.x -= VEL
        facing_left = True
        facing_right = False

    elif keys_pressed[pygame.K_d] and knight_rec.x + knight_rec.width + VEL < WIDTH: #RIGHT
        standing = False
        knight_rec.x += VEL
        facing_left = False
        facing_right = True

    else:
        standing = True

    #####   UPDATES THE SPRITE AND HANDLES THE INDEX BASED ON THE VARIABLES GIVEN ABOVE    #####
    if standing == False and index >= walking_len:
        index = 0

    if pygame.time.get_ticks() - last_update > IMAGE_INTERVAL:
        last_update = pygame.time.get_ticks()
        if standing == False:
            index = (index + 1) % walking_len
        else:
            index = (index + 1) % idle_len

    if standing == False and facing_left == True:
        KnightMove = pygame.transform.flip(walking_spritesheet.parse_sprite(index), 180, 0)
    if standing == False and facing_right == True:
        KnightMove = walking_spritesheet.parse_sprite(index)
    if standing == True and facing_left == True:
        KnightMove = pygame.transform.flip(idle_spritesheet.parse_sprite(index), 180, 0)
    if standing == True and facing_right == True:
        KnightMove = idle_spritesheet.parse_sprite(index)

    return KnightMove

def main():     
    clock = pygame.time.Clock()
    run = True
    knight_rec = pygame.Rect(0, 0, 64, 45)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        draw_window(knight_movement(keys_pressed, knight_rec), knight_rec)
    
    pygame.quit()

if __name__ == "__main__":
    main()

#draw_window(sprite_attack(index)) this was used to pass the sprite_attack animation into the draw_window function. index was used a var in the main() function to iterate over the loop.
#index = (index + 1) % attack_spritesheet_len
# def sprite_attack(index):
#     KnightDeath = attack_spritesheet.parse_sprite(index)
#     return KnightDeath.convert()

# attack_spritesheet = Spritesheet(cwd + "/sprites/noBKG_KnightAttack_strip.png")
# attack_spritesheet_len = len(attack_spritesheet.data["frames"]) 
#idle_spritesheet_len = len(idle_spritesheet.data["frames"]) 