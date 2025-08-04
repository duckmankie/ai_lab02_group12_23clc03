from helper_01 import *
from helper_02 import *

def run_solver(method, input_path, output_path):
    matrix = read_input_matrix(input_path)

    if method == "sat":
        ok, result = solve_with_pysat(matrix)
        if ok:
            write_output_matrix(result, output_path)
            print("Solved by SAT!")
        else:
            print("No solution using SAT.")
    
    elif method == "astar":
        result = solve_with_astar(matrix)
        if result:
            write_output_matrix(result, output_path)
            print("Solved by A*!")
        else:
            print("No solution using A*.")
    
    elif method == "brute":
        result = solve_with_bruteforce(matrix)
        if result:
            write_output_matrix(result, output_path)
            print("Solved by Brute-force!")
        else:
            print("No solution using Brute-force.")
    
    elif method == "backtrack":
        result = solve_with_backtracking(matrix)
        if result:
            write_output_matrix(result, output_path)
            print("Solved by Backtracking!")
        else:
            print("No solution using Backtracking.")
    
    else:
        print(f"Unknown method: {method}")


if __name__ == "__main__":
    input_file = "Inputs/input-01.txt"
    output_file = "Outputs/output-01.txt"

    while True:
        print("\nChọn phương pháp giải:")
        print("1. SAT")
        print("2. A*")
        print("3. Brute-force")
        print("4. Backtracking")
        print("0. Thoát")
        choice = input("Nhập số (0-4): ").strip()

        if choice == "0":
            print("Đã thoát chương trình.")
            break

        method_map = {
            "1": "sat",
            "2": "astar",
            "3": "brute",
            "4": "backtrack"
        }
        method = method_map.get(choice)
        if method:
            run_solver(method, input_file, output_file)
        else:
            print("Lựa chọn không hợp lệ.")