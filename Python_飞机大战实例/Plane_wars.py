"""自学飞机大战项目练习"""


import pygame
# import time


def main():
    # 1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((640, 1136), 0, 32)
    # 2.创建一个跟窗口大小一致的图片，用来填充当背景
    background = pygame.image.load("./spritesheets/background_2.png")
    # 创建一个我方飞机的图片，和上面一样
    hero = pygame.image.load("./spritesheets/hero_fly_1.png")
    # 3.把背景图片放到窗口中显示
    while True:
        # 设定需要显示的图在窗口中哪个位置显示
        screen.blit(background, (0, 0))
        screen.blit(hero, (252, 968))

        # 更新需要显示的内容
        pygame.display.update()
        # time.sleep(5)


if __name__ == '__main__':
    main()
