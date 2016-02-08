""" Read the input file and return a matrix
of 0's and 1's.
"""


def get_input_matrix(filename):
    f = open(filename)
    # remove the first line.
    f.readline()
    content = f.readlines()
    matrix = []
    for line in content:
        new_line = []
        for i in line:
            if i == '.':
                i = 0
                new_line.append(i)
            elif i == '#':
                i = 1
                new_line.append(i)

        matrix.append(new_line)
    f.close()

    return matrix
