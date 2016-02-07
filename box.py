def findBigSquare(array, height, width):
    """finds the biggest collection of shaded cells in a square"""
    for row_i, row in enumerate(array):

        span = findFirstLast(row)
        if span is None:
            continue

        first, last = span

        extRight = scanRight(array, height, width, row_i, first)
        extLeft = scanLeft(array, height, width, row_i, last)

        if extLeft is None:
            if extRight is None:
                return None
            else:
                r0, c0 = row_i, first
                r1, c1 = extRight

                if not confirmLeft(array, height, width, r0, c0, r1, c1):
                    return None

                return (r0, c0, r1, c1)
        else:
            if extRight is None:
                r0, c0 = row_i, last
                r1, c1 = extLeft

                if not confirmRight(array, height, width, r0, c0, r1, c1):
                    return None

                return (r0, c0, r1, c1)
            else:
                r1, c1 = extLeft
                r2, c2 = extRight

                if r1 > r2:
                    r0, c0 = row_i, first

                    if not confirmLeft(array, height, width, r0, c0, r1, c1):
                        return None

                    return (r0, c0, r1, c1)
                else:
                    r0, c0 = row_i, last

                    if not confirmRight(array, height, width, r0, c0, r1, c1):
                        return None

                    return (r0, c0, r2, c2)

def scanRight(array, height, width, row_i, col_i):
    """looks for the point furthest diagonaly right or returns None"""

    last_point = None

    while row_i++ < height and col_i++ < width:
        cell = array[row_i][col_i]

        if cell:
            last_point = (row_i, col_i)

    return last_point

def scanLeft(array, height, width, row_i, col_i):
    """looks for the point furthest diagonaly left or returns None"""
    
    last_point = None

    while row_i-- < height and col_i-- < width:
        cell = array[row_i][col_i]

        if cell:
            last_point = (row_i, col_i)

    return last_point

def confirmLeft(array, height, width, r0, c0, r1, c1):
    """confirms there is a point across on the left"""
    r2  = r0
    c2 = c1

    return array[r2][c2] ? True : False

def confirmRight(array, height, width, r0, c0, r1, c1):
    """confirms there is a point across on the right"""
    r2 = r1,
    c2 = c0

    return array[r2][c2] ? True : False

def findFirstLast(array):
    """finds two points furthest apart on a row"""

    first = None,
    last = None

    for i in range(0, array.len()):
        if array[i]:
            if first is None:
                first = i
            else
                last = i

        if first is None and last is None:
            return None
        else:
            return (first, last)