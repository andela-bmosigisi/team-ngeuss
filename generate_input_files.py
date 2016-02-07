"""Usage:

Generates problem specific input files in the current directory.

To generate 20 files
python generate_input_files.py 20
"""

import sys
import random

files_number = int(sys.argv[1])
file_names = []

for i in range(files_number):
    file_names.append('file_' + str(i) + '.in')

for j in range(files_number):
    f = open('input/' + file_names[j], 'w+')
    cols = random.randint(100, 800)
    rows = random.randint(20, 200)
    f.write(str(rows) + ' ' + str(cols) + '\n')
    for row in range(rows):
        line = [''] * cols
        for col in range(cols):
            line[col] = '#' if random.randint(0, 1) == 1 else '.'
        line = ''.join(line)
        f.write(line + '\n')
    f.close()
