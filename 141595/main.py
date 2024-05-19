from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

lose1 = GameSprite('me.jpg', 200, 200, 240, 270, 0)
lose2 = GameSprite('me.jpg', 200, 200, 240, 270, 0)

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_i] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_k] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > W_h:
            self.rect.x = randint(80, W_w - 80)
            self.rect.y = 0
            self.speed = randint(1, 7)
            lost = lost + 1

back = (177, 240, 209)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))


#отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('me.jpg', 30, 200, 4, 50, 6)
racket2 = Player('me.jpg', 520, 200, 4, 50, 6)
ball = GameSprite('me.jpg', 300, 0, 4, 50, 50)
m_x = 2
m_y = 2
#
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += m_x
        ball.rect.y += m_y
    racket1.reset()
    racket2.reset()
    ball.reset()
    if sprite.collide_rect(ball, racket1) or sprite.collide_rect(ball, racket2):
        m_x *= (-1)

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        m_y *= -1
    display.update()
    clock.tick(FPS)