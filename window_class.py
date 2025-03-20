from tkinter import Tk, BOTH, Canvas
from point_line_classes import Point, Line
from cell_class import Cell

## This class will handle the windows.
class Window:
    def __init__(self, w, h):
        self.__root = Tk()
        self.__root.title = ("Super Fabolous Regg44 Maze Solver Supreme")
        self.__window = Canvas(self.__root, bg="white", height=h, width=w)
        self.__window.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    ## "redraw" Method will update the window
    def redraw(self):
        self.__window.update_idletasks()
        self.__window.update()
    ## "wait_for_close" Method will call "redraw" while self.__running is True (while self.close hasn't been called.)
    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
    ## "close" Method will function as a way to set self.__running to false.
    def close(self):
        self.__running = False
    ## "draw_line" Method will create a line in canvas based on a Line instance and the self.__window canvas.
    def draw_line(self, Line, fill_color="black"):
        Line.draw(self.__window, fill_color)
