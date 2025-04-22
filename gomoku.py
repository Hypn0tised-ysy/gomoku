import pygame
import sys
from chessboard import Chessboard

from pygame.locals import QUIT,KEYDOWN

#TODO 可以改成枚举变量  
#color
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
GRAY = [169, 169, 169]
LIGHT_GRAY = [211, 211, 211]
DARK_GREEN = [0, 100, 0]
CHEST_BACKGROUND=[239, 152, 81]
RECT_COLOR=[18, 111, 216]

#screen size 
#board size
SCREEN_SIZE=670
MARGIN=30
PIECE_SIZE=20
#每行落子数，暂时想不到什么好名字，因为有棋盘中心的概念，需要是奇数
PLAY_REGION_SIZE=15

def draw_line(screen, chessboard):
    margin = chessboard.margin
    size = chessboard.size
    offset = chessboard.offset
    n = chessboard.play_region_size
    line_color=chessboard.line_color
    line_width=chessboard.line_width

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
    
def draw_important_pos(screen,chessboard):
    center=chessboard.center

    margin = chessboard.margin
    size = chessboard.size
    offset = chessboard.offset
    n = chessboard.play_region_size
    line_color=chessboard.line_color
    line_width=chessboard.line_width
 
    left_bottom=(margin, margin)
    right_bottom=(size-margin, margin)
    left_top=(margin, size-margin)
    right_top=(size-margin, size-margin)

    x1=(left_bottom[0]+center[0])/2
    x2=(right_bottom[0]+center[0])/2

    y1=(left_top[1]+center[1])/2
    y2=(left_bottom[1]+center[1])/2

    pygame.draw.circle(screen,line_color,center,line_width*4,0)
    # pygame.draw.circle(screen,line_color,(x1,y1),line_width*4,1)
    # pygame.draw.circle(screen,line_color,(x1,y2),line_width*4,1)
    # pygame.draw.circle(screen,line_color,(x2,y1),line_width*4,1)
    # pygame.draw.circle(screen,line_color,(x2,y2),line_width*4,1)

def draw_chessboard(screen,chessboard):
    draw_line(screen,chessboard)
    draw_important_pos(screen,chessboard)
    #画棋子
    for i in range(chessboard.play_region_size):
        for j in range (chessboard.play_region_size):
            if chessboard.get_occupied((i,j)):
                color =BLACK if chessboard.get_color((i,j)) == "black" else WHITE 
                pygame.draw.circle(screen,color,chessboard.get_pos((i,j)),PIECE_SIZE,0)
                
    
pygame.init()


screen = pygame.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))
screen_color=CHEST_BACKGROUND

line_color=BLACK
line_width=2

chessboard=Chessboard(SCREEN_SIZE,MARGIN ,PLAY_REGION_SIZE,screen_color,line_color,line_width)

piece_color=["black","white"]
steps=0

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            pygame.quit()
    screen.fill(screen_color)
    #
    x,y=pygame.mouse.get_pos()
    i,j=chessboard.get_index((x,y))
    #棋子x,y坐标
    x_piece,y_piece=chessboard.get_pos((i,j))
    pygame.draw.rect(screen, RECT_COLOR, (x_piece-PIECE_SIZE/2, y_piece-PIECE_SIZE/2, PIECE_SIZE, PIECE_SIZE), 1)
    
    win=False
    #鼠标左键防抖
    if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
        if chessboard.get_occupied((i,j))==False:
            chessboard.update_status((i,j),piece_color[steps%2])
            steps+=1
            win=chessboard.check_win((i,j))
    draw_chessboard(screen,chessboard)
    pygame.display.update()

    if win:
           print("win")
           pygame.time.wait(1000)  # Wait for 1 second to show the win message
           font = pygame.font.Font(None, 74)
           text = font.render("WIN!", True, (255, 0, 0))  # Red color for win message
           text_rect = text.get_rect(center=(SCREEN_SIZE // 2, SCREEN_SIZE // 2))
           screen.blit(text, text_rect)
           pygame.display.update()
           while True:
                for event in pygame.event.get():
                       if event.type in (QUIT, KEYDOWN):
                            pygame.quit()


    
    
