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

        assert len(lines) == 5, "len(lines): {0}".format(len(lines))

        assert (1, 2, 1, 5) == lines[0], "lines[0]: {0}".format(lines[0])
        assert (2, 2, 2, 5) == lines[1], "lines[1]: {0}".format(lines[1])
        assert (6, 3, 6, 5) == lines[4], "lines[4]: {0}".format(lines[4])

    def testYLine(self):
        lines = scan_y_lines(self.grid)

        assert len(lines) == 4, "len(lines): {0}".format(len(lines))

        assert (1, 2, 5, 2) == lines[0], "lines[0]: {0}".format(lines[0])
        assert (1, 3, 6, 3) == lines[1], "lines[1]: {0}".format(lines[1])
        assert (1, 5, 6, 5) == lines[3], "lines[3]: {0}".format(lines[3])

    def testBox(self):
        boxes = scan_boxes(self.grid)

        assert len(boxes) == 5, "len(boxes): {0}".format(boxes)

        assert (1, 2, 3, 4) == boxes[0], "boxes[0]: {0}".format(boxes[0])
        assert (1, 3, 3, 5) == boxes[1], "boxes[1]: {0}".format(boxes[1])
        assert (2, 2, 4, 4) == boxes[2], "boxes[2]: {0}".format(boxes[2])
        assert (2, 3, 4, 5) == boxes[3], "boxes[3]: {0}".format(boxes[3])
        assert (4, 3, 6, 5) == boxes[4], "boxes[4]: {0}".format(boxes[4])


