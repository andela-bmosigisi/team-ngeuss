import unittest

from .scans import *

class ScansTestCase(unittest.TestCase):

    def setUp(self):
        array = [
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0]
        ]

        height = 7
        width = 7

        self.grid = array, height, width

    def tearDown(self):
        pass

    def testXLine(self):
        lines = scan_x_lines(self.grid)

        self.assertEqual( len(lines), 5)

        self.assertEqual( (1, 2, 1, 5), lines[0])
        self.assertEqual( (2, 2, 2, 5), lines[1])
        self.assertEqual( (6, 3, 6, 5), lines[4])

    def testYLine(self):
        lines = scan_y_lines(self.grid)

        self.assertEqual( len(lines), 4)

        self.assertEqual( (1, 2, 5, 2), lines[0])
        self.assertEqual( (1, 3, 6, 3), lines[1])
        self.assertEqual( (1, 5, 6, 5), lines[3])

    def testBox(self):
        boxes = scan_boxes(self.grid)

        self.assertEqual( len(boxes), 5)

        self.assertEqual( (1, 2, 3, 4), boxes[0])
        self.assertEqual( (1, 3, 3, 5), boxes[1])
        self.assertEqual( (2, 2, 4, 4), boxes[2])
        self.assertEqual( (2, 3, 4, 5), boxes[3])
        self.assertEqual( (4, 3, 6, 5), boxes[4])

    def testAABB(self):
        pass

    def testScan(self):
        scan(self.grid)