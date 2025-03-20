from tkinter import Canvas

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_1, point_2):
        self.p1 = point_1
        self.p2 = point_2
    def draw(self, canvas, fill_color="Black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
