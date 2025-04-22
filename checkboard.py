import pygame

class Checkboard:
    def __init__(self,size=670, margin=5,  play_region_size=15 ,background_color="white",line_color="black",line_width=2):
        #
        self.margin = margin
        #棋盘大小
        self.size = size
        #
        self.background_color = background_color
        self.line_color=line_color
        self.line_width=line_width
        # 每行每列最大落子数
        self.play_region_size = play_region_size
        self.fresh_board_size()
    
    def cal_offset(self):
        self.offset=(self.size-2*self.margin)/self.play_region_size

    def set_size(self,size):
        self.size=size
        self.fresh_board_size()

    def set_margin(self, margin):
        self.margin = margin
        self.fresh_board_size()

    def set_background_color(self, background_color):
        self.background_color = background_color

    def set_line_color(self,line_color):
        self.line_color=line_color

    def set_line_width(self,line_width):
        self.line_width=line_width

    def set_play_region_size(self, play_region_size):
        self.play_region_size = play_region_size
        self.fresh_board_size()

    def cal_center(self):
        x=self.margin + self.offset * (self.play_region_size - 1) / 2
        self.center = (x,x)
    def fresh_board_size(self):
        self.cal_offset()
        self.cal_center()