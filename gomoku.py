import pygame
import sys
from checkboard import Checkboard

from pygame.locals import QUIT,KEYDOWN

def draw_line(screen, checkboard, line_width):
    margin = checkboard.margin
    size = checkboard.size
    offset = checkboard.offset
    n = checkboard.play_region_size
    line_color=checkboard.line_color
 
    left_bottom=(margin, margin)
    right_bottom=(size-margin, margin)
    left_top=(margin, size-margin)
    right_top=(size-margin, size-margin)
    
    # 绘制外边框（四条边）
    border_lines = [
        (left_bottom, right_bottom), (left_top, right_top),
        (left_bottom, left_top), (right_bottom, right_top)
   ]
    for start, end in border_lines:
        pygame.draw.line(screen, line_color, start, end, line_width * 2)

    # 绘制内部网格线
    for i in range(n):
        x = margin + offset * i
        y = margin + offset * i
        # 垂直线
        pygame.draw.line(screen, line_color, (x, margin), (x, size - margin), line_width)
        # 水平线
        pygame.draw.line(screen, line_color, (margin, y), (size - margin, y), line_width)
    

pygame.init()

#TODO 可以改成枚举变量  
#color
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
GRAY = [169, 169, 169]
LIGHT_GRAY = [211, 211, 211]
DARK_GREEN = [0, 100, 0]
CHEST_BACKGROUD=[239, 152, 81]

#screen size 
#board size
SCREEN_SIZE=670
MARGIN=30
#每行落子数，暂时想不到什么好名字，因为有棋盘中心的概念，需要是奇数
PLAY_REGION_SIZE=15

screen = pygame.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))
screen_color=CHEST_BACKGROUD

line_color=BLACK
line_width=2

checkboard=Checkboard(SCREEN_SIZE,MARGIN ,PLAY_REGION_SIZE,screen_color,line_color,line_width)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill(screen_color)
    draw_line(screen,checkboard,line_width)
    pygame.display.update()
    
    
