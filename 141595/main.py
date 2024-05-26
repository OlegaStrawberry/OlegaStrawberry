from pygame import *
from random import randint

#переменные важно
font.init()
font2 = font.SysFont('serif', 40)
score = 0
nine = 9
win_width = 600
win_height = 500
game = True
finish = False
clock = time.Clock()
FPS = 60
m_x = -4
m_y = 2

#классы
#Класс родитель
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

#Класс наследник. ракетки!!
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

#картинки
#фоны
background = transform.scale(image.load("heaven.jpg"), (win_width, win_height))
background1 = transform.scale(image.load("desert.jpg"), (win_width, win_height))
background2 = transform.scale(image.load("les.jpg"), (win_width, win_height))
background3 = transform.scale(image.load("stairway.jpg"), (win_width, win_height))
background4 = transform.scale(image.load("concert.jpg"), (win_width, win_height))
background5 = transform.scale(image.load("Stepa.jpg"), (win_width, win_height))
background6 = transform.scale(image.load("StepanJPG.jpg"), (win_width, win_height))
background7 = transform.scale(image.load("TARDIS.jpg"), (win_width, win_height))
background8 = transform.scale(image.load("myboys.jpg"), (win_width, win_height))
window = display.set_mode((win_width, win_height))
#проигрыш левого
lose1 = GameSprite('lose2.png', 200, 200, 350, 350, 0)
#проигрыш правого
lose2 = GameSprite('lose1.png', 200, 200, 350, 350, 0)
#левая ракетка
racket1 = Player('rack1.png', 30, 200, 100, 150, 6)
#правая ракетка
racket2 = Player('rack2.png', 450, 200, 100, 150, 6)
#мяч
ball = GameSprite('ball.png', 300, 0, 75, 75, 50)

while game:
    if score < 15:
        window.blit(background, (0, 0))
    if score >= 15 and score < 30:
        window.blit(background7, (0, 0))
    if score >= 30 and score < 45:
        window.blit(background6, (0, 0))
    if score >= 45 and score < 60:
        window.blit(background8, (0, 0))
    if score >= 60 and score < 75:
        window.blit(background4, (0, 0))
    if score >= 75 and score < 90:
        window.blit(background5, (0, 0))
    if score >= 90 and score < 100:
        window.blit(background1, (0, 0))
    if score >= 100 and score < 110:
        window.blit(background2, (0, 0))
    if score >= 110:
        window.blit(background3, (0, 0))
    racket1.reset()
    racket2.reset()
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        text = font2.render("Счёт:" + str(score), 1, (214, 137, 201))
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

    if ball.rect.y > win_height-50 or ball.rect.y < -10:
        m_y *= -1
    if ball.rect.x <= -70:
        lose1.reset()
        text = font2.render("Счёт:" + str(score), 1, (214, 137, 201))
        window.blit(text, (10, 20))
        finish = True
    if ball.rect.x >= 600:
        lose2.reset()
        text = font2.render("Счёт:" + str(score), 1, (214, 137, 201))
        window.blit(text, (10, 20))
        finish = True
    
    ball.reset()
    display.update()
    clock.tick(FPS)