import pygame
import json
import os

global index
global facing_left
global facing_right
index = 0
facing_left = False
facing_right = True
VEL = 5

class Character:
    
    def __init__(self,filename):
    
        self.character = filename
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.meta_data = self.character.replace("png", "json")
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()
    
    #"/sprites/noBKG_KnightIdle_strip.png")
    def load (self, file):
        pass

    def get_sprite(self, x, y, w, h):
        BLACK = (0,0,0)
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((BLACK))
        sprite.blit(self.sprite_sheet,(0,0),(x, y, w, h))
        return sprite
    
    def parse_sprite(self, index):
        sprite = self.data["frames"][index]["frame"]
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        self.index = 0
        return image

