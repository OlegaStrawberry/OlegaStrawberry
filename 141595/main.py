from pygame import *
from random import randint

font.init()
font2 = font.SysFont('Arial', 40)
score = 0
nine = 9
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
        if keys[K_k] and self.rect.y < win_height - 140:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 140:
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

win_width = 600
win_height = 500
background = transform.scale(image.load("heaven.jpg"), (win_width, win_height))
background1 = transform.scale(image.load("desert.jpg"), (win_width, win_height))
background2 = transform.scale(image.load("les.jpg"), (win_width, win_height))
background3 = transform.scale(image.load("stairway.jpg"), (win_width, win_height))
background4 = transform.scale(image.load("concert.jpg"), (win_width, win_height))
background5 = transform.scale(image.load("Stepa.jpg"), (win_width, win_height))
window = display.set_mode((win_width, win_height))

#отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('rack1.png', 30, 200, 100, 150, 6)
racket2 = Player('rack2.png', 450, 200, 100, 150, 6)
ball = GameSprite('ball.png', 300, 0, 75, 75, 50)
m_x = -4
m_y = 2
#
while game:
    if score < 15:
        window.blit(background, (0, 0))
    if score >= 15:
        window.blit(background2, (0, 0))
    if score >= 30:
        window.blit(background1, (0, 0))
    if score >= 45:
        window.blit(background3, (0, 0))
    if score >= 60:
        window.blit(background4, (0, 0))
    if score >= 75:
        window.blit(background5, (0, 0))
    if score >= 90:
        window.blit(background6, (0, 0))
    racket1.reset()
    racket2.reset()
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        text = font2.render("Счёт:" + str(score), 1, (41, 71, 87))
        window.blit(text, (10, 20))

        racket1.update_l()
        racket2.update_r()
        ball.rect.x += m_x
        ball.rect.y += m_y
    
    if sprite.collide_rect(ball, racket1) or sprite.collide_rect(ball, racket2):
        if nine > 0:
            nine -= 0.1
        m_x *= (-1)
        m_x += 0.1
        ball.rect.x += nine * m_x
        score = score + 1



        

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        m_y *= -1
    if ball.rect.x <=0:
        lose1.reset()
    if ball.rect.x >= 600:
        lose2.reset()
    
    ball.reset()
    display.update()
    clock.tick(FPS)

    