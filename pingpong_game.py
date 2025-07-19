from pygame import *

background_img = 'jellyfishbg.jpg'
player1_image = 'spongebob.png'
ball_img = 'jellyfish.png'
player2_image = 'patrick.png'

win_height = 500
win_width = 700 
window = display.set_mode((win_width, win_height))
display.set_caption('Jellyfishing!')
background = transform.scale(image.load(background_img), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player1(GameSprite):
    def update_1(self):
        keys = key_pressed = key.get_pressed()
        if key_pressed [K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if key_pressed [K_s] and self.rect.x < win_width - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update_r(self):
        keys = key_pressed = key.get_pressed()
        if key_pressed [K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if key_pressed [K_DOWN] and self.rect.x < win_width - 80:
            self.rect.y += self.speed

ball = GameSprite(ball_img, 100, 200, 50, 70, 5)
racket_1 = Player1(player1_image, 20, 200, 80, 100, 2)
racket_r = Player2(player2_image, 600, 200, 80, 100, 2)

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        ball.reset()
        racket_1.reset()
        racket_r.reset()

        racket_1.update_1()
        racket_r.update_r()

        display.update()
