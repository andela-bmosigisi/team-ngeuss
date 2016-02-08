"""Usage:

Generates a specified number of input files in the input/ directory.

To generate 20 files
python generate_input_files.py 20
"""

import os
import sys
import random

files_number = int(sys.argv[1])
file_names = []

for i in range(files_number):
    file_names.append('file_' + str(i) + '.in')

if not os.path.exists('input'):
    os.makedirs('input')

for j in range(files_number):
    f = open('input/' + file_names[j], 'w+')
    cols = random.randint(100, 800)
    rows = random.randint(20, 200)
    f.write(str(rows) + ' ' + str(cols) + '\n')
    for row in range(rows):
        line = [''] * cols
        # increase the bias towards the dot.
        toggler = random.randint(0, 100) >= 90
        for col in range(cols):
            if (toggler):
                line[col] = '#'
            else:
                line[col] = '.'
            # Give the toggler a chance of toggling its value.
            if (random.randint(1, 100) > 97):
                toggler = False if toggler else True
        line = ''.join(line)
        f.write(line + '\n')
    f.close()
