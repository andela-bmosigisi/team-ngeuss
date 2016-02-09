from greedy.greedy import *
from generate_matrix import get_input_matrix
from serializer.command_generator import generate_command
import sys
import os

if __name__ == '__main__':
    # Receive the filename from the console args.
    filename = sys.argv[1]

    matrix = get_input_matrix(filename)
    line_1 = ''
    with open(filename) as f:
        line_1 = f.readline()
    line_1 = line_1.split(' ')

    if not os.path.exists('output'):
        os.makedirs('output')

    output_file_name = filename[-7:-3] + '.out'
    output_file = open('output/output_'+output_file_name, 'w+')
    rows_num = int(line_1[0])
    cols_num = int(line_1[1])
    while (not check_matrix_empty(matrix, rows_num, cols_num)):
        # draw all the big squares.
        l_s = get_largest_square(matrix)
        while (l_s is not None):
            # l_s contains the center and size.
            offset = (l_s[2] - 1) / 2
            r0 = l_s[0] - offset
            r1 = l_s[0] + offset
            c0 = l_s[1] - offset
            c1 = l_s[1] + offset

            for r in range(r0, r1 + 1):
                for c in range(c0, c1 + 1):
                    matrix[r][c] = 0

            command = generate_command((r0, c0, r1, c1))
            output_file.write(command + '\n')
            l_s = get_largest_square(matrix)

        # draw all the lines.
        l_l = get_longest_line(matrix)
        while (l_l is not None):
            for ro in range(l_l[0], l_l[2] + 1):
                for co in range(l_l[1], l_l[3] + 1):
                    matrix[ro][co] = 0

            command = generate_command((l_l[0], l_l[1], l_l[2], l_l[3]))
            output_file.write(command + '\n')
            l_l = get_longest_line(matrix)

        # draw the remaining cells
        for i in range(0, rows_num):
            for j in range(0, cols_num):
                if (matrix[i][j] == 1):
                    command = generate_command((i, j, i, j))
                    output_file.write(command + '\n')
                    matrix[i][j] = 0

    output_file.close()
