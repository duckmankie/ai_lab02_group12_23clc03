from helper_01 import *
from helper_02 import *

if __name__ == "__main__":
    matrix = read_input_matrix("Inputs/input-01.txt")

    # DÙNG SAT (nếu muốn)
    # ok, result = solve_with_pysat(matrix)
    

    # DÙNG A*
    result = solve_with_astar(matrix)
    if result:
        write_output_matrix(result, "Outputs/output-01.txt")
        print("Solved by A*!")
    else:
        print("No solution.")
