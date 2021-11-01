#https://oco.itch.io/medieval-fantasy-character-pack?download
import pygame
from spritesheet import Spritesheet
import json
pygame.display.set_caption("First Game!")

WIDTH, HEIGHT = (900,500)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
WHITE = (255,255,255)
VEL = 5
attack_spritesheet = Spritesheet("/home/ben/first_pygame/Assets/noBKG_KnightAttack_strip.png")
attack_spritesheet_len = len(attack_spritesheet.data["frames"])         
idle_spritesheet = Spritesheet("/home/ben/first_pygame/Assets/noBKG_KnightIdle_strip.png")
idle_spritesheet_len = len(idle_spritesheet.data["frames"])    
KnightMove = idle_spritesheet.parse_sprite(0)

def sprite_attack(index):
    KnightDeath = attack_spritesheet.parse_sprite(index)
    return KnightDeath.convert()

def draw_window(knight_rec):
    WIN.fill((WHITE))
    WIN.blit(KnightMove, (knight_rec.x, knight_rec.y))
    #WIN.blit(image, ((0,0)))
    pygame.display.update()
    
def knight_movement(keys_pressed, knight_rec):
    if keys_pressed[pygame.K_a] and knight_rec.x - VEL > 0: # LEFT
        knight_rec.x -= VEL
    if keys_pressed[pygame.K_d] and knight_rec.x + knight_rec.width + VEL < WIDTH: # RIGHT
        knight_rec.x += VEL
    if keys_pressed[pygame.K_w] and knight_rec.y - VEL > 0: # UP
        knight_rec.y -= VEL
    if keys_pressed[pygame.K_s] and knight_rec.y + knight_rec.height + VEL < HEIGHT: # DOWN
        knight_rec.y += VEL
    
def main(): 
    index = 0
    clock = pygame.time.Clock()
    run = True
    knight_rec = pygame.Rect(0, 0, 64, 45)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        knight_movement(keys_pressed, knight_rec)
        
        draw_window(knight_rec)
    
    pygame.quit()

if __name__ == "__main__":
    main()

#draw_window(sprite_attack(index)) this was used to pass the sprite_attack animation into the draw_window function. index was used a var in the main() function to iterate over the loop.
#index = (index + 1) % attack_spritesheet_len