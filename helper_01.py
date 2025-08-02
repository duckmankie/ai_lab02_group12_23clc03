def read_input_matrix(filename):
    matrix = []
    file = open(filename, 'r')
    for line in file:
        cells = line.strip().split(',')
        row = []
        for cell in cells:
            row.append(int(cell))
        matrix.append(row)
    file.close()
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for cell in row:
            print(cell, end=' ')
        print()

def write_output_matrix(matrix, filename):
    file = open(filename, 'w')
    for row in matrix:
        line = ''
        for index in range(len(row)):
            line += str(row[index])
            if index != len(row) - 1:
                line += ', '
        file.write(line + '\n')
    file.close()