import pygame

chess_piece={
    "index":(-1,-1),
    "pos":(-1,-1),
    "occupied":False,
    "color":None

}

# 默认正方形棋盘
class Chessboard:
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

        #维护落子状态
        self.init_status()
    
    def init_status(self):
        #i,j 不是行列，按坐标索引，类似于（x，y）
        self.status = [[{
            "index": (i, j),
            "pos": (self.margin + i * self.offset, self.margin + j * self.offset),
            "occupied": False,
            "color": None
        } for j in range(self.play_region_size)] for i in range(self.play_region_size)]
    
    def get_pos(self,index):
        return self.status[index[0]][index[1]]["pos"]
    def get_occupied(self,index): 
        return self.status[index[0]][index[1]]["occupied"]
    def get_color(self,index):
        return self.status[index[0]][index[1]]["color"]
    
    def cal_offset(self):
        self.offset=(self.size-2*self.margin)/(self.play_region_size-1)

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
    def map_to_index(self, coord):
        x, y = coord
        # Clamp x and y to be within the board limits
        x = max(self.margin, min(x, self.size - self.margin))
        y = max(self.margin, min(y, self.size - self.margin))

        # Calculate the relative positions
        rel_x = (x - self.margin) / self.offset
        rel_y = (y - self.margin) / self.offset

        # Clamp the relative positions to be within the grid
        rel_x = max(0, min(rel_x, self.play_region_size - 1))
        rel_y = max(0, min(rel_y, self.play_region_size - 1))

        return (rel_x, rel_y)
        
    # 写二分查找写到一般突然发现可以用常数时间算出来...
    def get_index(self,coord):
        rel_x,rel_y=self.map_to_index(coord)
        return round(rel_x),round(rel_y)
    
    def update_status(self,index,color):
        x,y=index
        self.status[x][y]["occupied"]=True
        self.status[x][y]["color"]=color

    def check_win(self, index):
        x, y = index
        min_index, max_index = 0, self.play_region_size - 1
        color = self.status[x][y]["color"]
        
        # 辅助函数：检查一个方向上的连续棋子数量
        def check_direction(dx, dy):
            count = 1
            tmp_x, tmp_y = x, y
            
            # 向一个方向扩展
            while 0 <= tmp_x + dx <= max_index and 0 <= tmp_y + dy <= max_index and self.get_color((tmp_x + dx, tmp_y + dy)) == color:
                tmp_x += dx
                tmp_y += dy
                count += 1
            
            return count
        
        # 1. 检查水平方向
        count = check_direction(-1, 0) + check_direction(1, 0) - 1  # 左右方向
        if count >= 5:
            return True
        
        # 2. 检查垂直方向
        count = check_direction(0, 1) + check_direction(0, -1) - 1  # 上下方向
        if count >= 5:
            return True
        
        # 3. 检查左上到右下方向
        count = check_direction(-1, 1) + check_direction(1, -1) - 1  # 左上到右下方向
        if count >= 5:
            return True
        
        # 4. 检查右上到左下方向
        count = check_direction(1, 1) + check_direction(-1, -1) - 1  # 右上到左下方向
        if count >= 5:
            return True
        
        return False
