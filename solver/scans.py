import itertools

def scan_x_lines(grid):
    """an x line is a posibbly incomplete horizontal line

    for example [0 0 0 1 1 1 0 0] or [0 0 1 0 1 0 0 0] are
    both lines of length 3

    """

    array, _, _ = grid
    
    lines = []

    for r, row in enumerate(array):
        start, end = scan_row(row)
        if end - start > 1:
            r0, c0, r1, c1 = (r, start, r, end)
            lines.append((r0, c0, r1, c1))

    return lines

def scan_y_lines(grid):
    """a y line is a posibbly incomplete vertical line

    for example
        1 0 0       1 0 0
        1 0 0  or   0 0 0
        1 0 0       1 0 0

    both lines of length 3

    """
    array, height, width = grid

    new_array = [[row[i] for row in array] for i in range(0, width)]

    new_grid = (new_array, width, height)

    x_lines = scan_x_lines(new_grid)

    y_lines = [(c0, r1, c1, r0) for r0, c0, r1, c1 in x_lines]

    return y_lines

def scan_boxes(grid):
    """a box is a posibbly incomplete cardinaly odd square

    for example
        0 1 1 1 0       0 0 1 1 0
        0 1 1 1 0   or  0 1 1 1 0
        0 1 1 1 0       0 1 0 1 0
        0 0 0 0 0       0 0 0 0 0
    are both cube squares

    """
    array, height, width = grid

    boxes = []

    def fit(r, c):
        r0, c0 = (r, c)
        opposite = scan_across_right(grid, r, c)
        adjacent = scan_across_left(grid, r, c)

        if opposite is not None:
            r1, c1 = opposite
            if  r1 - r0 > 1:
                if array[r1][c0]:
                    boxes.append((r0, c0, r1, c1))

        if adjacent is not None:
            r1, c1 = adjacent
            if r1 - r0 > 1:
                if array[r1][c0]:
                    boxes.append((r0, c1, r1, c0))

    for r, row in enumerate(array):
        start, end = scan_row(row)
        if end - start > 1:
            fit(r, start)
            fit(r, end)

    return boxes

def scan_row(row):
    """get the first and last shaded columns in a row"""

    start = 0
    end = 0

    for c, value in enumerate(row):
        if value:
            if start == 0:
                start = c
            end = c

    return (start, end)

def scan_across_right(grid, row_i, col_i):
    """find the furtherst shaded cell diagonaly down right"""

    array, height, width = grid
    last_point = None

    while row_i < height and col_i < width:
        if array[row_i][col_i]:
            last_point = (row_i, col_i)

        row_i += 2
        col_i += 2

    return last_point

def scan_across_left(grid, row_i, col_i):
    """find the furtherst shaded cell diagonaly down left"""

    array, height, width = grid
    last_point = None

    while row_i < height and col_i > 0:
        if array[row_i][col_i]:
            last_point = (row_i, col_i)

        row_i += 2
        col_i -= 2

    return last_point

def aabb(shape1, shape2):
    """test if shapes are overlapping"""
    r0, c0, r1, c1 = shape1
    r2, c2, r3, c3 = shape2

    return c1 >= c2 and c3 >= c0 and r1 >= r2 and r3 >= r0 

def score(grid, shape):
    """score the significance of the shape

    a shapes value is how many shaded cells it covers
    against how many it covers but are unshaded.
    """
    array, _, _ = grid
    r0, c0, r1, c1 = shape
    points = 0

    for r in range(r0, r1):
        for c in range(c0, c1):
            if array[r][c]:
                points+=1

    return points

def filter_shapes(grid, shapes):
    """remove shapes of least value"""

    collision_list = {}
    filtered = []

    for shape0, shape1 in itertools.permutations(shapes, 2):
        if aabb(shape0, shape1):
            try:
                collision_list[shape0].append(shape1)
            except KeyError:
                collision_list[shape0] = []
                collision_list[shape0].append(shape1)

    for shape in collision_list:
        own_weight = score(grid, shape)
        others_weight = sum(map(lambda s:score(grid, s), collision_list[shape]))

        if own_weight >= others_weight:
            filtered.append(shape)
    return filtered

def scan_unshader(grid, shapes):
    """find cells covered by shape but unshaded"""

    array, _, _ = grid
    unshade = []

    for shape in shapes:
        r0, c0, r1, c1 = shape

        for r in range(r0, r1):
            for c in range(c0, c1):
                if not array[r][c]:
                    unshade.append((r, c))

def scan_shader(grid, shapes):
    """find cells uncovered by shape but shaded"""

    array, height, width = grid
    shade = []

    for r in range(0, height):
        for c in range(0, width):
            if array[r][c]:

                collision = False
                for shape in shapes:
                    if aabb(shape, (r, c, r, c)):
                        collision = True
                        break

                if not collision:
                    shade.append((r, c))

    return shade

def scan(grid):
    """extract minimum required shapes to describe grid

    this produces two lists, one of shapes to draw
    and the other of areas to erase
    """
    x_lines = scan_y_lines(grid)
    y_lines = scan_y_lines(grid)
    boxes = scan_boxes(grid)

    shapes = x_lines + y_lines + boxes

    shades = filter_shapes(grid, shapes)

    unshades = scan_unshader(grid, shades)

    shades.append(scan_shader(grid, shades))

