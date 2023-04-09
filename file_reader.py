from pygame import *
window = display.set_mode((700, 500))
display.set_caption('amogus')
run = True
back = (240, 128, 128)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 620:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.right, self.rect.centery, 15, 20, 15)
        bullets.add(bullet)

class Enemy(GameSprite):
    side = 'left'

    def update(self):
        if self.rect.x <= 420:
            self.side = 'right'
        if self.rect.x >= 615:
            self.side = 'left'
        if self.rect.x == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= 710:
            self.kill()

player = Player('hero.png', 5, 420, 5, 80, 80)
wall1 = GameSprite('platform1.png', 700/2 - 700/3, 500 / 2, 0, 300, 50)
wall2 = GameSprite('platform2.png', 370, 100, 0, 50, 400)
monster = Enemy('enemy.png', 620, 180, 5, 80, 80)
treasure = GameSprite('treasure.png', 615, 400, 0, 80, 80)

barriers = sprite.Group()
bullets = sprite.Group()
monsters = sprite.Group()

monsters.add(monster)
barriers.add(wall1)
barriers.add(wall2)
finish = False
while run:
    time.delay(50)
    window.fill(back)
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if finish != True:
        
        player.reset()
        barriers.draw(window)
        player.update()
        monster.reset()
        monster.update()
        treasure.reset()
        display.update()
    display.update()
