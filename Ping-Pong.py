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
            self.rect.y -= self.speed
        if keys[pg.K_s] and self.rect.y < 350:
            self.rect.y += self.speed

    def update_right(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed


pg.init()
window = pg.display.set_mode((600, 500))
pg.display.set_caption('Ping-Pong')
game = True
speed_x = 1
speed_y = 2
finish = False
pg.font.init()
font = pg.font.Font(None, 34)
win_left = font.render('Левый игрок выиграл!', True, (0, 0, 0))
win_right = font.render('Правый игрок выиграл!', True, (0, 0, 0))
background = pg.image.load('Background.png')
racket_left = Player('racket.png', 50, 150, 30, 200, 2)
racket_right = Player('racket.png', 50, 150, 520, 200, 2)
ball = GameSprite('tenis_ball.png', 50, 50, 275, 230, 1)

while game:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        racket_left.reset()
        racket_right.reset()
        ball.reset()
        racket_left.update_left()
        racket_right.update_right()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if pg.sprite.collide_rect(ball, racket_left) or pg.sprite.collide_rect(ball, racket_right):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y == 440 or ball.rect.y < 20:
            speed_y *= -1
            speed_x *= 1
        if ball.rect.x <= -30:
            finish = True
            window.blit(win_right, (200, 200))
        if ball.rect.x >= 590:
            finish = True
            window.blit(win_left, (200, 200))

    pg.display.update()