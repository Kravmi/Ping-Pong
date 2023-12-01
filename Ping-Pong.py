import pygame as pg 


class GameSprite(pg.sprite.Sprite):
    def __init__(self, image, width, height, x, y, speed):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_left(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[pg.K_s] and self.rect.y < 620:
            self.rect.x += self.speed

    def update_right(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[pg.K_DOWN] and self.rect.y < 620:
            self.rect.x += self.speed


pg.init()
window = pg.display.set_mode((600, 500))
pg.display.set_caption('Ping-Pong')
game = True

while game:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            game = False