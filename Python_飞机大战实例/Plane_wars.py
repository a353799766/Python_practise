"""自学飞机大战项目练习"""


import pygame
# import time
from pygame.locals import *  # 用来检测事件，比如键盘按键操作


def main():
    # 1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((640, 1136), 0, 32)
    # 2.创建一个跟窗口大小一致的图片，用来填充当背景
    background = pygame.image.load("./spritesheets/background_2.png")
    # 创建一个我方飞机的图片，和上面一样
    hero = pygame.image.load("./spritesheets/hero_fly_1.png")
    # 3.把背景图片放到窗口中显示
    x = 252
    y = 968
    while True:
        # 设定需要显示的图在窗口中哪个位置显示
        screen.blit(background, (0, 0))
        screen.blit(hero, (x, y))
        # 获取事件，比如按键等
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
                    x -= 5
                # 检测按键是否是d或者方向键right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    x += 5
                elif event.key == K_w or event.key == K_UP:
                    print('up')
                    y -= 5
                elif event.key == K_s or event.key == K_DOWN:
                    print('down')
                    y += 5
                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')
        # 更新需要显示的内容
        pygame.display.update()
        # time.sleep(5)


if __name__ == '__main__':
    main()
