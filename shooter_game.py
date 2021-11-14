from pygame import *
from random import *
score = 0
lost = 0
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size, size1 ):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size, size1))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
                self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 10, 10, 30)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 525:
            self.rect.y = 0
            self.rect.x = randint(5, 700)
            global lost
            lost += 1
class Bullet(GameSprite):
    def update(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed
        else:
            self.kill()
monsters = sprite.Group()
bullets = sprite.Group()
for i in range(4):
    monster = Enemy("asteroid.png", randint(0, 650), -10, randint(1,2), 50, 50)
    monsters.add(monster)
clock = time.Clock()

FPS = 60
window = display.set_mode((700, 500))
display.set_caption("Шутер")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
player = Player("rocket.png", 350, 400, 10, 50, 100)
game = True
font.init()
font = font.SysFont("Arial", 25)
while game:
    window.blit(background, (0, 0))
    for i in event.get():
        if i.type == QUIT:
            game = False
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                player.fire()
    collides = sprite.groupcollide(monsters, bullets, True, True)
    for c in collides:
        score += 1
        monster = Enemy("asteroid.png", randint(0, 650), -10, randint(1, 2), 50, 50)
        monsters.add(monster)
    sprite_lost = font.render("Пропущено: " + str(lost), True, (255, 255, 255))
    sprite_num = font.render("Сбито: " + str(score), True, (255, 255, 255))
    window.blit(sprite_lost, (5, 5))
    window.blit(sprite_num, (5, 30))
    monsters.draw(window)
    monsters.update()
    bullets.draw(window)
    bullets.update() 
    monsters.update()
    player.reset() 
    player.update()     
    clock.tick(FPS)    
    display.update()