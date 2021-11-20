from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = image.load(player_image)
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s]:
            if self.rect.y < height - 148:
                self.rect.y += self.speed
            else:
                self.rect.y = height - 148
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed
        if keys[K_DOWN]:
            if self.rect.y < height - 148:
                self.rect.y += self.speed
            else:
                self.rect.y = height - 148
       
init()
width = int(display.Info().current_w)
height = int(display.Info().current_h)
clock = time.Clock()
FPS = 60
#window = display.set_mode((700, 500))
window = display.set_mode()
#display.set_caption("Пинг-понг")
background = transform.scale(image.load("background.bmp"), (width, height))
game = True
player1 = Player("player.bmp", 10, width / 2, 10)
player2 = Player("player.bmp", width - 25, width / 2, 10)
font.init()
font = font.SysFont("Arial", 25)
while game:
    window.blit(background, (0, 0))
    for i in event.get():
        if i.type == QUIT:
            game = False
    player1.reset()
    player1.update()
    player2.reset()
    player2.update1()
    clock.tick(FPS)    
    display.update()
