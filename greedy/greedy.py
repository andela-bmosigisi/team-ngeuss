"""Collection of functions used for the greedy
algorithm.
"""


def get_largest_square(matrix):
    """ Get the largest square whose size is greater than 1.

    Args:
        matrix - multi-dimensional list of 0's and 1's

    Returns a tuple describing the biggest square's center coordinates
    and the dimensions of the cell.
        e.g (2, 3, 5) is a size 4 centered at (2, 3)
        (r, c, s)
    If none is found, it returns None.
    """
    rows_no = len(matrix)
    cols_no = len(matrix[0])
    if (rows_no < 3 or cols_no < 3):
        return None
    largest_square = None
    for r in range(0, rows_no):
        for c in range(0, cols_no):
            sq = scan_square(r, c, matrix)
            if (sq is None):
                continue
            if (largest_square is None):
                largest_square = sq
                continue
            if (sq[2] > largest_square[2]):
                largest_square = sq

    return largest_square


def scan_square(row, col, matrix):
    """ Scan the current position for a square of odd sides.
    Args:
        row - integer for row position
        col - column position
        matrix - multi-dimensional list of 0's and 1's

    Returns a tuple describing the biggest square's center coordinates
    and the dimensions of the cell.
        e.g (2, 3, 5) is a size 4 centered at (2, 3)
        (r, c, s)
    Return None if none is found.
    """
    if (matrix[row][col] == 0):
        return None

    sq = None
    rows_no = len(matrix)
    cols_no = len(matrix[0])
    found = True
    for step in range(2, rows_no+cols_no, 2):
        r1 = row + step
        c1 = col + step
        if (r1 > rows_no or c1 > cols_no):
            break
        for r in range(row, r1):
            for c in range(col, c1):
                if (matrix[r][c] == 0):
                    found = False
                    break
        if (found is True):
            sq = ((row + r1)/2, (col + c1)/2, r1-row + 1)

    return sq


def get_longest_line(matrix):
    """ Scans the whole matrix to find the longest line,
        whether it is vertical or horizontal.

    Args:
        matrix - multi-dimensional list of 0's and 1's

    Returns a tuple describing the two cells which bind the longest line.
    e.g (2, 4, 2, 20) starts at (2, 4) and ends at (2, 20)
    (r1, c1, r2, c2)
    """
    # scan the horizontal space
    longest_line = None
    size = 0
    rows_no = len(matrix)
    for i in range(0, rows_no):
        row_as_string = ''.join([str(f) for f in matrix[i]])
        in_i = scan_line(row_as_string)
        if (in_i is None):
            continue
        horizontal_size = in_i[1] - in_i[0]
        if (horizontal_size > size):
            size = horizontal_size
            longest_line = (i, in_i[0], i, in_i[1])

    cols_no = len(matrix[1])
    # scan the vertical space.
    for j in range(0, cols_no):
        # create a new list for a column.
        vertical = []
        for k in range(0, rows_no):
            vertical.append(matrix[k][j])
        col_as_string = ''.join([str(i) for i in vertical])
        in_v = scan_line(col_as_string)
        if (in_v is None):
            continue
        size_v = in_v[1] - in_v[0]
        if (size_v > size):
            size = size_v
            longest_line = (in_v[0], j, in_v[1], j)

    return longest_line


def scan_line(line_as_string):
    """Find the longest consecutive 1's in a line.

    Args:
        matrix - multi-dimensional list of 0's and 1's

    Returns a tuple describing the two columns where longest line lies.
    """
    one = '1'
    match = line_as_string.find(one * 2)
    if (match == -1):
        return None

    longest = (match, match+1)
    str_len = len(line_as_string)
    for i in range(3, str_len):
        match = line_as_string.find(one * i)
        if (match != -1):
            longest = (match, match + i - 1)

    return longest


def check_matrix_empty(matrix, rows, cols):
    """ Return True if the matrix is made up of 0's"""
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                return False

    return True
