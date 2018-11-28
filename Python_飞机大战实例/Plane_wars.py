"""自学飞机大战项目练习"""


import pygame
import time
from pygame.locals import *  # 用来检测事件，比如键盘按键操作
import random


class BasePlane(object):
    """定义飞机的基类"""

    def __init__(self, x, y, screen, image_path):
        self.x = x
        self.y = y
        self.screen = screen
        self.bullet_list = []
        self.image = pygame.image.load(image_path)  # 创建一个飞机的图片

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


class Hero(BasePlane):
    """定义我方飞机类"""

    def __init__(self, screen):
        BasePlane.__init__(self, 140, 488, screen, "./spritesheets/hero_fly_1.png")

    # 在窗口显示飞机，并显示射击子弹
    def display(self):
        BasePlane.display(self)
        # 显示子弹,为什么写在这里，而不是写在shoot方法里,如果写在shoot里，只会显示一次就消失
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.y < 0:
                bullet.delete()  # 调用删除子弹的方法

    # 以下4个方法是控制上下左右
    def move_right(self):
        self.x += 5

    def move_left(self):
        self.x -= 5

    def move_down(self):
        self.y += 5

    def move_up(self):
        self.y -= 5

    def shoot(self):
        # 创建子弹对象,对象有三个属性，并保存在列表中。注意这里并没有在main函数里创建子弹
        self.bullet_list.append(
            Bullets(
                self.screen,
                self.x,
                self.y,
                self,
                self.bullet_list))


class Enemy(BasePlane):
    """定义敌方飞机类"""

    def __init__(self, screen):
        BasePlane.__init__(self, 0, 0, screen, "./spritesheets/enemy1_fly_1.png")
        self.position = "right"

    # 在窗口显示飞机
    def display(self):
        BasePlane.display(self)
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.y > 540:
                bullet.delete()  # 调用删除子弹的方法

    def move(self):
        """移动敌机，并判断敌机的边界值"""
        if self.position == "right":
            self.x += 2
            # self.y += 1
        elif self.position == "left":
            self.x -= 2
            # self.y += 1
        if self.x > 320 - 38:
            self.position = "left"
        elif self.x < 0:
            self.position = "right"

    def shoot(self):
        # 创建子弹对象,对象有三个属性，并保存在列表中。注意这里并没有在main函数里创建子弹
        # 利用random来控制发射子弹
        random_num = random.randint(1, 400)
        if random_num == 32 or random_num == 111:
            self.bullet_list.append(
                EnemyBullets(
                    self.screen,
                    self.x,
                    self.y,
                    self,
                    self.bullet_list))


class BaseBullet(object):
    def __init__(self, x, y, screen, image_path, plane_temp, bullet_list):
        # x，y经过下方计算后，子弹才会在飞机的正上方显示
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(image_path)  # 创建一个子弹图片，和上面一样
        self.plane = plane_temp
        self.bullet_list = bullet_list

    def display(self):
        """显示子弹"""
        self.screen.blit(self.image, (self.x, self.y))

    def delete(self):
        self.bullet_list.remove(self)


class Bullets(BaseBullet):
    """定义我方飞机子弹类"""

    def __init__(self, screen, x, y, hero, bullet_list):
        BaseBullet.__init__(self, x + 34, y - 20, screen, "./spritesheets/bullet1.png", hero, bullet_list)

    def move(self):
        """通过while和空格键控制移动子弹"""
        self.y -= 5


class EnemyBullets(BaseBullet):
    """定义敌方飞机子弹类"""

    def __init__(self, screen, x, y, enemy, bullet_list):
        BaseBullet.__init__(self, x+19, y+30, screen, "./spritesheets/bullet2.png", enemy, bullet_list)

    def move(self):
        self.y += 1


def key_control(hero_temp):
    """控制键盘的函数"""
    for event in pygame.event.get():
        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            # 检测按键是否是d或者方向键right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            elif event.key == K_w or event.key == K_UP:
                print('up')
                hero_temp.move_up()
            elif event.key == K_s or event.key == K_DOWN:
                print('down')
                hero_temp.move_down()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.shoot()  # 这里应该是飞机.显示子弹方法（）


def main():
    # 1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((320, 568), 0, 32)
    # 2.创建一个跟窗口大小一致的图片，用来填充当背景
    background = pygame.image.load("./spritesheets/background_2.png")
    hero = Hero(screen)  # 创建我方飞机英雄对象
    enemy = Enemy(screen)
    while True:
        # 设定需要显示的图在窗口中哪个位置显示
        screen.blit(background, (0, 0))
        # 我方飞机英雄显示
        hero.display()
        # 敌方飞机显示
        enemy.display()
        enemy.move()
        enemy.shoot()
        # 获取事件，比如按键等
        key_control(hero)
        # 更新需要显示的内容
        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
