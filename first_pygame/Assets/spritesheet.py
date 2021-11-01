import pygame
import json


class Spritesheet:
    
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.meta_data = self.filename.replace("png", "json")
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()

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
        return image
