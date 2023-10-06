from pygame import*
init()
# розмір вікна
W = 700
H = 700
# створили вікно
window = display.set_mode((W, H))

display.set_caption("labyrinth")
display.set_icon(image.load('treasure.png'))

back = transform.scale(image.load('background.jpg'), (W, H))
clock = time.Clock()

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.4)
mixer.music.play()

kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self, player_imp, player_x, player_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_imp), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()#отримуємо список отриманих клавіш
        if keys_pressed[K_w] and self.rect.y > 0:# перевірка клавіши у верх
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < H - 65:# перевіряємо клавішу у низ
            self.rect.y += self.speed
            
        if keys_pressed[K_a] and self.rect.x > 0:# перевіряємо клавіши в вліво
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < W - 65:# перевіряємо клавішу право
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = "right"# напрямок руху ворога
    
    def update(self, start, end):
        if self.rect.x >= end:# якщо ми доходимо до кінця 
            self.direction = 'left'# міняємо напрямок в ліво
            self.image = transform.scale(image.load('cyborg_l.png'), (65, 65))# змінюємо на картинку яка повернута вліво
        if self.rect.x <= start:# якщо ми доходимо до початку
            self.direction = 'right'# міняємо напрямок в право
            self.image = transform.scale(image.load('cyborg.png'), (65, 65))# змінюємо на картинку яка повернута в право
        
        if self.direction == 'left':# ідемо вліво
            self.rect.x -= self.speed
        if self.direction == 'right':# ідемо в право
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_w, wall_h, wall_x, wall_y):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.widht = wall_w
        self.height = wall_h
        self.image = Surface((self.widht, self.height))
        self.image.fill((self.color1, self.color2, self.color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

gold = GameSprite('treasure.png', 550, 550, 0) 
hero = Player('hero.png', 40, 40, 3)
enemy = Enemy('cyborg.png', 350, 400, 2)
game = True
# рамка
wall1 = Wall(108, 126, 130, 680, 10, 10, 20)
wall2 = Wall(108, 126, 130, 10, 660, 10, 20)
wall3 = Wall(108, 126, 130, 670, 10, 20, 670)
wall4 = Wall(108, 126, 130, 10, 660, 680, 20)
# лабіринт
wall5 = Wall(108, 126, 130, 60, 10, 20, 120)
wall6 = Wall(108, 126, 130, 10, 180, 160, 30)
wall7 = Wall(108, 126, 130, 120, 10, 160, 120)
wall8 = Wall(108, 126, 130, 120, 10, 260, 200)
wall9 = Wall(108, 126, 130, 10, 100, 380, 30)
wall10 = Wall(108, 126, 130, 10, 100, 380, 200)
wall11 = Wall(108, 126, 130, 100, 10, 380, 120)
wall12 = Wall(108, 126, 130, 10, 100, 480, 120)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(back, (0, 0))
    gold.reset()
    hero.reset()
    hero.update()
    enemy.reset()
    enemy.update(350, 450)
    wall1.reset()
    wall2.reset()
    wall3.reset()
    wall4.reset()
    wall5.reset()
    wall6.reset()
    wall7.reset()
    wall8.reset()
    wall9.reset()
    wall10.reset()
    wall11.reset()
    wall12.reset()
    if sprite.collide_rect(hero, wall1) or sprite.collide_rect(hero, wall2) or sprite.collide_rect(hero, wall3) or sprite.collide_rect(hero, wall4) or sprite.collide_rect(hero, wall5) or sprite.collide_rect(hero, wall6) or sprite.collide_rect(hero, wall7) or sprite.collide_rect(hero, wall8) or sprite.collide_rect(hero, wall9) or sprite.collide_rect(hero, wall10) or sprite.collide_rect(hero, enemy):
        hero.rect.x = 20
        hero.rect.y = 40
    if sprite.collide_rect(hero, gold):
        game = False
    display.update()
    clock.tick(60)