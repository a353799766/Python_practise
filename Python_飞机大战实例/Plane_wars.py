"""自学飞机大战项目练习"""


import pygame
import time
from pygame.locals import *  # 用来检测事件，比如键盘按键操作


class Hero(object):
    """定义我方飞机类"""
    def __init__(self):
        self.x = 140
        self.y = 488
        self.image = pygame.image.load(
            "./spritesheets/hero_fly_1.png")  # 创建一个我方飞机的图片，和上面一样

    # 在窗口显示飞机
    def display(self, screen_temp):
        screen_temp.blit(self.image, (self.x, self.y))

    # 以下4个方法是控制上下左右
    def move_right(self):
        self.x += 5

    def move_left(self):
        self.x -= 5

    def move_down(self):
        self.y += 5

    def move_up(self):
        self.y -= 5


class Bullets(object):
    def __init__(self):
        self.x = 140
        self.y = 488
        self.image = pygame.image.load(
            "./spritesheets/bullet1.png")  # 创建一个子弹图片，和上面一样

    def display(self, screen_temp):
        screen_temp.blit(self.image, (self.x, self.y))


def key_control(hero_temp,):
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
                pass  # 这里应该是飞机.显示子弹方法（）


def main():
    # 1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((320, 568), 0, 32)
    # 2.创建一个跟窗口大小一致的图片，用来填充当背景
    background = pygame.image.load("./spritesheets/background_2.png")
    hero = Hero()  # 创建我方飞机英雄对象
    bullets = Bullets()
    while True:
        # 设定需要显示的图在窗口中哪个位置显示
        screen.blit(background, (0, 0))
        # 我方飞机英雄显示
        hero.display(screen)
        # 获取事件，比如按键等
        key_control(hero)
        # 更新需要显示的内容
        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
