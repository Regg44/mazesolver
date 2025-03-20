from cell_class import Cell
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_colums, cell_size_x, cell_size_y, win=None, seed=None,):
        # Initialize all data members to class.
        self._cells = [] # This one in particular will save the cells in the maze.
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_colums = num_colums
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed != None:
            self._seed = seed
        else:
            self._seed = random.seed(seed)

        # Iniate "_create_cells" from the get-go
        self._create_cells()
        

        self._break_entrance_and_exit()

        self._break_walls_r(0,0)

        self._reset_cells_visited()
    
    # Method to create the cells inside the Maze, this is why we dont put grid logic on the cells themselves, the maze class will handle it.
    def _create_cells(self):
        rows = []
        
        for c in range(self._num_colums):
            rows = []
            for r in range(self._num_rows):
                rows.append(Cell(self._win))
            self._cells.append(rows)
        print(self._cells)
        
        for col in range(len(self._cells)):
            for row in range(len(self._cells[col])):
                self._draw_cell(col, row)
    # This method is not supposed to draw the full maze, instead, it draws a single cell depending on its column and row.
    def _draw_cell(self, i, j):
        if self._win == None:
            return
        # i is column, j is row
        x1 = self._x1 + i*self._cell_size_x
        y1 = self._y1 + j*self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate()

    
    
    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(0.001)

    def _break_entrance_and_exit(self):
            self._cells[0][0].left_wall = False
            self._draw_cell(0,0)
            self._cells[self._num_colums -1][self._num_rows - 1].right_wall = False
            self._draw_cell(self._num_colums -1, self._num_rows - 1)
            print(self._cells[0][0].left_wall, self._cells[self._num_colums -1][self._num_rows - 1].right_wall)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            adj_cells = []
            if i < self._num_colums - 1:
                if not self._cells[i+1][j].visited:
                    adj_cells.append([i+1,j])
            if i > 0:
                if not self._cells[i-1][j].visited:
                    adj_cells.append([i-1,j])
            if j < self._num_rows - 1:
                if not self._cells[i][j+1].visited:
                    adj_cells.append([i,j+1])
            if j > 0:
                if not self._cells[i][j-1].visited:
                    adj_cells.append([i,j-1])
            
            if len(adj_cells) == 0:
                self._draw_cell(i,j)
                return
                
            next_cell = random.choice(adj_cells)
            

            if next_cell[0] == i - 1:
                self._cells[i][j].left_wall = False
                self._cells[next_cell[0]][next_cell[1]].right_wall = False
            if next_cell[0] == i + 1:
                self._cells[i][j].right_wall = False
                self._cells[next_cell[0]][next_cell[1]].left_wall = False
            if next_cell[1] == j - 1:
                self._cells[i][j].top_wall = False
                self._cells[next_cell[0]][next_cell[1]].bottom_wall = False
            if next_cell[1] == j + 1:
                self._cells[i][j].bottom_wall = False
                self._cells[next_cell[0]][next_cell[1]].top_wall = False
            print(adj_cells)
            print(next_cell)
            self._break_walls_r(next_cell[0], next_cell[1])


    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self._num_colums - 1 and j == self._num_rows - 1:
            return True
        
        if  j > 0 and self._cells[i][j].top_wall == False and self._cells[i][j-1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i,j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
        
        if j < self._num_rows - 1 and self._cells[i][j].bottom_wall == False and self._cells[i][j+1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i,j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
        
        if i < self._num_colums - 1 and self._cells[i][j].right_wall == False and self._cells[i+1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
        
        if i > 0 and self._cells[i][j].left_wall == False and self._cells[i-1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)

        return False
        
    def solve(self):
        return self._solve_r(i=0,j=0)

    






