# Разработай свою игру в этом файле!
from pygame import * 
from pygame import * 
import time as tm 
font.init()
#создание глав. окна
wW = 1280
wH = 720 

mainWindow = display.set_mode((wW, wH))
display.set_caption('Лабиринт')
mainWindow.fill((255, 255, 255))
background = transform.scale(image.load('fon.png'), (wW, wH))

#класс для обектов 
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, widht, height):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(img), (widht, height))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

    def show(self):
        mainWindow.blit(self.image, (self.rect.x, self.rect.y))
#класс для глав героя
class Hero(GameSprite):
    def __init__(self, img, x, y, widht, height, speed):
        GameSprite.__init__(self, img, x, y, widht, height)
        self.speed = speed
        self.gravity = 10
        self.JumpCount = 4.4
        self.isJump = False
        self.standImage = transform.scale(image.load('yese.png'), (widht, height))
        self.jumpImage = transform.scale(image.load('jamp.png'), (widht, height))
        self.rightImage = transform.scale(image.load('WALK12.png'), (widht, height))
        self.leftImage = transform.flip(self.rightImage, True, False)
        self.doorOpen = False
        self.heveKey = False

    def update(self):
        keys = key.get_pressed()
        if keys[K_d]:
            self.rect.x += self.speed
            self.image = self.rightImage

        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
            self.image = self.leftImage

    def jump(self):
        keys = key.get_pressed()
        if keys[K_SPACE]:
            self.isJump = True
            self.image = self.jumpImage

        if self.isJump:
            self.rect.y -= self.JumpCount ** 2
            self.JumpCount -= 0.2
            if self.JumpCount <= 0:
                self.isJump = False 
                self.JumpCount = 4

    def falling(self):
        if sprite.spritecollide(self, walls, False):
            platformsTouched = sprite.spritecollide(self, walls, False)
            for platform in platformsTouched:
                if platform.rect.top < self.rect.bottom:
                    self.gravity = 0
                    if self.isJump == False:
                        self.image = self.standImage
        else:
            if self.isJump == False:
                self.gravity = 10

class Enymy(GameSprite):
     def __init__(self, img, x, y, widht, height, speed, pointLeft, pointRight):
        GameSprite.__init__(self, img, x, y, widht, height)
        self.pointLeft = pointLeft
        self.speed = speed
        self.pointRight = pointRight
        self.direction = 'LEFT'
        def update(self):
            self.direction = 'LEFT'
            if self.rect.x <= self.pointLeft:
                self.direction = 'RIGHT'
            elif self.rect.x >= self.pointRight:
                self.direction = 'LEFT'
            
            if self.direction == 'LEFT':
                self.rect.x -= self.speed
            elif self.direction == 'RIGHT':
                self.rect.x += self.speed

#создание объектов
player = Hero('yese.png', 50, 400, 66, 82, 8)
spider1 = Enymy('spider.png', 750, 415, 71, 45, 4, 700, 950)
spider2 = Enymy('spider.png', 220, 270, 71, 45, 1, 200, 400)
door = GameSprite('door_closedMid.png', 20, 120, 70, 70)
point = GameSprite('keyYellow.png', 1000, 800, 44, 40)


#платформы
walls = sprite.Group()
#палтформы  1ряд
platformX = 0
for i in range(19):
    wall = GameSprite('shroomTanMid.png', platformX, 600, 70, 70)
    walls.add(wall)
    platformX += 70
#палтформы  2ряд
platformX = 640
for i in range(10):
    wall = GameSprite('shroomTanMid.png', platformX, 465, 70, 70)
    walls.add(wall)
    platformX += 70
#платформа 3 рад
platformX = 200
for i in range(3):
    wall = GameSprite('shroomTanMid.png', platformX, 300, 70, 70)
    walls.add(wall)
    platformX += 70
# Игравой цикл 
fps = 60
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    mainWindow.blit(background, (0, 0))
    door.show()
    point.show()
    player.show()
    walls.draw(mainWindow)
    if sprite.collide_rect(player, point):
        plaer.haveaKey = True
        if point.rect.y > 20:
            point.rect.y -= 20
    if sprite.collide_rect(player, door):
        if player.haveaKey:
            plaeyr.doorOpen = True
    if player.doorOpen:
        door.image = image.load('door_openMid.png', )
        exitText = font.SysFont('verdana', 18).render('press enter to going', True, (255, 255, 255))
        mainWindow.blit(exitText, (door.rect.left, door.rect.top - 30))
    
    player.falling()
    player.jump()
    player.update()
    player.rect.y += player.gravity


    display.update()
    clock.tick(fps)
    spider1.show()
    spider2.show()





































