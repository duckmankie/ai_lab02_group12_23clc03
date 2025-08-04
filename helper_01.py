from itertools import product

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

def generate_cnf(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    variable_to_id = {}
    id_to_variable = {}
    clauses = []
    var_count = 1

    def make_var(pos1, pos2, bridge_count):
        nonlocal var_count
        key = (min(pos1, pos2), max(pos1, pos2), bridge_count)
        if key not in variable_to_id:
            variable_to_id[key] = var_count
            id_to_variable[var_count] = key
            var_count += 1
        return variable_to_id[key]

    neighbor_map = {}
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] <= 0:
                continue
            pos = (r, c)
            neighbor_map[pos] = []
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                while 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[nr][nc] > 0:
                        neighbor_map[pos].append((nr, nc))
                        break
                    elif matrix[nr][nc] == 0:
                        nr += dr
                        nc += dc
                    else:
                        break

    for pos in neighbor_map:
        expected = matrix[pos[0]][pos[1]]
        total_vars = []
        for neighbor in neighbor_map[pos]:
            a, b = sorted([pos, neighbor])
            for count in [1, 2]:
                var_id = make_var(a, b, count)
                total_vars.append((count, var_id))

        valid_combinations = []
        for combo in product([0, 1], repeat=len(total_vars)):
            total = sum(weight for (weight, var_id), use in zip(total_vars, combo) if use)
            if total == expected:
                clause = []
                for (weight, var_id), use in zip(total_vars, combo):
                    clause.append(var_id if use else -var_id)
                valid_combinations.append(clause)

        clauses.extend(valid_combinations)

    return clauses, variable_to_id, id_to_variable

