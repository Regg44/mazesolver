from point_line_classes import Point, Line
class Cell:
    def __init__(self, win=None):
        # We add a "Visted" parameter as a data member to track cell status when generating maze.
        
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.visited = False
        ## x1 and y1 represent top left corner and x2-y2 represent bottom right corner
        self.x1 = None 
        self.y1 = None
        self.x2 = None
        self.y2 = None
        ## _win apparently is the window, lol.
        self._win = win
    def draw(self, x1, y1, x2, y2): ## We create points for every corner of the cell. Not the most efficient, but the easier for the eyes.
        if self._win is None:
            return
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        point_tl = Point(self.x1, self.y1)
        point_tr = Point(self.x2, self.y1)
        point_bl = Point(self.x1, self.y2)
        point_br = Point(self.x2, self.y2)
        
        # Instead of generating the line when it exists, we generate them all and then update the color depending if it exists.
        lwall = Line(point_tl, point_bl)
        rwall = Line(point_tr, point_br)
        twall = Line(point_tl, point_tr)
        bwall = Line(point_bl, point_br)
        if self.left_wall:
            self._win.draw_line(lwall)
        else:
            self._win.draw_line(lwall, "white")

        if self.right_wall:
            self._win.draw_line(rwall)
        else:
            self._win.draw_line(rwall, "white")

        if self.top_wall:
            self._win.draw_line(twall)
        else:
            self._win.draw_line(twall, "white")

        if self.bottom_wall:
            self._win.draw_line(bwall)
        else:
            self._win.draw_line(bwall, "white")
            
            
    
    def draw_move(self, to_cell, undo=False):
        # We set the centers based on the averages of the points, not sure if it'll work, test need be.
        center1 = Point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
        center2 = Point((to_cell.x1 + to_cell.x2) / 2, (to_cell.y1 + to_cell.y2) / 2)
        line_ctc = Line(center1, center2)

        # Set for line to be red on default, if "undo" flag is set, then it'll be gray
        line_color = "red"
        if undo:
            line_color = "gray"
        # Draw method should perhaps be on self._win itself, will be changed if needed.
        
        self._win.draw_line(line_ctc, line_color)

    def __repr__(self):
        if self.visited:
            return "v"
        return "o"


