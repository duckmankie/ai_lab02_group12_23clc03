from helper_01 import *
from helper_02 import *

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
            timed_run_solver(method, input_file, output_file)
        else:
            print("Lựa chọn không hợp lệ.")