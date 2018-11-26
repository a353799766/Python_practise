"""飞机大战第一个版本:显示窗口和背景"""


import pygame
import time


def main():
    # 1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # 2.创建一个跟窗口大小一致的图片，用来填充当背景
    background = pygame.image.load("./Resource/background.jpg")
#     3.把背景图片放到窗口中显示
    while True:
        # 设定需要显示的背景图在窗口中哪个位置显示
        screen.blit(background, (0, 0))
        # 更新需要显示的内容
        pygame.display.update()
        # time.sleep(5)


if __name__ == '__main__':
    main()
