from window_class import Window, Point, Line
from cell_class import Cell
from maze_class import Maze

##Example Window
win = Window(800, 600)

##Example Line
example_line = Line(point_1=Point(25, 25), point_2=Point(50, 50))

##We call draw_line from window class
# win.draw_line(example_line, "blue")

example_cell = Cell(win)
example_cell.x1, example_cell.y1, example_cell.x2, example_cell.y2 = 25, 50, 50, 25
example_cell.left_wall = False


m1 = Maze(10, 30, 20, 20, 6, 6, win)
m1.solve()


##We call "wait_for_close" to innitiate program.
win.wait_for_close()
print(m1._cells)
m1._reset_cells_visited()
print(m1._cells)

