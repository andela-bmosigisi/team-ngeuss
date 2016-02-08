import unittest
from .command_generator import generate_command as gc


class TestCommandGenerator(unittest.TestCase):

    def test_erase_cell(self):
        self.assertEqual(gc((), (4, 5)), 'ERASE_CELL 4 5')
        self.assertEqual(gc((1, 2, 3, 4), (19, 5)),
                         'ERASE_CELL 19 5')

    def test_paint_single_cell(self):
        self.assertEqual(gc((1, 2, 1, 2), None),
                         'PAINT_SQUARE 1 2 0')
        self.assertEqual(gc((4, 2, 4, 2)), 'PAINT_SQUARE 4 2 0')
        # Even negatives are fair game.
        self.assertEqual(gc((-2, 4, -2, 4)),
                         'PAINT_SQUARE -2 4 0')

    def test_paint_line(self):
        # paint vertical lines
        self.assertEqual(gc((1, 2, 4, 2)), 'PAINT_LINE 1 2 4 2')
        self.assertEqual(gc((0, 4, 3, 4)), 'PAINT_LINE 0 4 3 4')
        # paint horizontal lines
        self.assertEqual(gc((4, 5, 4, 9)), 'PAINT_LINE 4 5 4 9')
        self.assertEqual(gc((3, 9, 3, 3)), 'PAINT_LINE 3 9 3 3')

    def test_paint_large_squares(self):
        self.assertEqual(gc((1, 2, 3, 4)), 'PAINT_SQUARE 2 3 1')
        self.assertEqual(gc((0, 0, 4, 4)), 'PAINT_SQUARE 2 2 2')
        self.assertEqual(gc((5, 7, 11, 13)), 'PAINT_SQUARE 8 10 3')
