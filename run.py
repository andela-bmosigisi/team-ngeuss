with open('input.txt') as myfile:
    content = myfile.readlines()
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

print matrix
