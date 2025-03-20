import unittest
from maze_class import Maze
from window_class import Window

win = Window(800, 1200)
class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(10, 30, num_rows, num_cols, 10, 10, win)
        m1._break_entrance_and_exit()
        m1._animate()
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

if __name__ == "__main__":
    unittest.main()
