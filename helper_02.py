from pysat.solvers import Solver
from helper_01 import generate_cnf
from copy import deepcopy
from collections import defaultdict,deque
import heapq

def solve_with_pysat(matrix):
    clauses, var_map, id_map = generate_cnf(matrix)
    max_var = max(var_map.values())
    with Solver(name='glucose3') as solver:
        for clause in clauses:
            solver.add_clause(clause)
        if solver.solve():
            model = solver.get_model()
            result = []
            for lit in model:
                if lit > 0 and lit in id_map:
                    result.append(id_map[lit])
            return True, result
        else:
            return False, []
        
class State:
    def __init__(self, matrix, bridges, cost):
        self.matrix = matrix  # bản sao input gốc
        self.bridges = bridges  # {(pos1, pos2): số cầu}
        self.cost = cost

    def is_goal(self):
        return self.all_islands_satisfied() and self.is_connected()

    def get_neighbors(self):
        neighbors = []
        rows = len(self.matrix)
        cols = len(self.matrix[0])

        # Duyệt tất cả ô là đảo (> 0)
        for r in range(rows):
            for c in range(cols):
                cell = self.matrix[r][c]
                if not isinstance(cell, int) or cell <= 0:
                    continue
                pos = (r, c)

                for dr, dc, bridge_char in [(-1, 0, "|"), (1, 0, "|"), (0, -1, "-"), (0, 1, "-")]:
                    nr, nc = r + dr, c + dc
                    path = []
                    end_pos = None

                    while 0 <= nr < rows and 0 <= nc < cols:
                        target = self.matrix[nr][nc]

                        if isinstance(target, int) and target > 0:
                            end_pos = (nr, nc)
                            break
                        elif target == 0:
                            path.append((nr, nc))
                        else:
                            break

                        nr += dr
                        nc += dc

                    if end_pos is None or not path:
                        continue  # không có đảo hoặc không có chỗ để đi cầu

                    key = tuple(sorted([pos, end_pos]))
                    current_bridge_count = self.bridges.get(key, 0)

                    if current_bridge_count >= 2:
                        continue  # đã đủ 2 cầu giữa cặp này

                    # Cho phép thêm 1 hoặc 2 cầu (nếu còn chỗ)
                    for add_count in [1, 2]:
                        if current_bridge_count + add_count > 2:
                            continue

                        new_matrix = deepcopy(self.matrix)
                        new_bridges = self.bridges.copy()

                        # Cập nhật cầu trên đường đi
                        for pr, pc in path:
                            if add_count == 1:
                                new_matrix[pr][pc] = bridge_char
                            else:
                                new_matrix[pr][pc] = "=" if bridge_char == "-" else "$"

                        # Cập nhật thông tin cầu
                        new_bridges[key] = current_bridge_count + add_count

                        # Tạo trạng thái mới
                        new_state = State(new_matrix, new_bridges, self.cost + add_count)
                        neighbors.append(new_state)

        return neighbors

    def heuristic(self):
        total_missing = 0
        bridge_count = defaultdict(int)

        # Đếm số cầu kết nối tới mỗi đảo từ self.bridges
        for (a, b), count in self.bridges.items():
            bridge_count[a] += count
            bridge_count[b] += count

        # Tính tổng số cầu còn thiếu trên toàn bộ đảo
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[0])):
                val = self.matrix[r][c]
                if isinstance(val, int) and val > 0:
                    connected = bridge_count[(r, c)]
                    missing = max(0, val - connected)
                    total_missing += missing

        return total_missing
        

    def all_islands_satisfied(self):

    # Đếm tổng số cầu nối tới mỗi đảo
        bridge_count = defaultdict(int)

        for (a, b), count in self.bridges.items():
            bridge_count[a] += count
            bridge_count[b] += count

        # Kiểm tra từng ô: nếu là đảo, thì tổng cầu phải đúng
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[0])):
                val = self.matrix[r][c]
                if isinstance(val, int) and val > 0:
                    if bridge_count[(r, c)] != val:
                        return False

        return True


    def is_connected(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        islands = set()

        # Bước 1: Lưu lại tất cả vị trí đảo
        for r in range(rows):
            for c in range(cols):
                if isinstance(self.matrix[r][c], int) and self.matrix[r][c] > 0:
                    islands.add((r, c))

        if not islands:
            return True  # không có đảo nào cũng coi là liên thông

        # Bước 2: Duyệt BFS từ một đảo bất kỳ
        visited = set()
        queue = deque()
        start = next(iter(islands))
        queue.append(start)
        visited.add(start)

        # Sử dụng self.bridges để biết các kết nối
        bridge_map = {}

        for (a, b), count in self.bridges.items():
            if count > 0:
                bridge_map.setdefault(a, []).append(b)
                bridge_map.setdefault(b, []).append(a)

        while queue:
            u = queue.popleft()
            for v in bridge_map.get(u, []):
                if v not in visited:
                    visited.add(v)
                    queue.append(v)

        # Bước 3: Kiểm tra xem đã đi qua hết các đảo chưa
        return visited == islands

    def __lt__(self, other):
        return (self.cost + self.heuristic()) < (other.cost + other.heuristic())

    def to_output_matrix(self):
        # Trả về ma trận hiển thị kết quả ["=", "-", "|", "$", số...]
        return self.matrix  # placeholder



def solve_with_astar(matrix):
    start = State(matrix, bridges={}, cost=0)
    open_set = []
    heapq.heappush(open_set, (start.cost + start.heuristic(), start))
    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)

        if current.is_goal():
            return current.to_output_matrix()

        for neighbor in current.get_neighbors():
            heapq.heappush(open_set, (neighbor.cost + neighbor.heuristic(), neighbor))

    return None

def solve_with_backtracking(matrix):
    start = State(matrix, bridges={}, cost=0)
    visited = set()

    def backtrack(state):
        # Nếu đạt trạng thái đích thì trả về kết quả
        if state.is_goal():
            return state.to_output_matrix()
        # Duyệt các trạng thái kế tiếp
        for neighbor in state.get_neighbors():
            # Để tránh lặp lại trạng thái, có thể dùng tuple hóa bridges
            bridges_tuple = tuple(sorted(neighbor.bridges.items()))
            if bridges_tuple in visited:
                continue
            visited.add(bridges_tuple)
            result = backtrack(neighbor)
            if result is not None:
                return result
            visited.remove(bridges_tuple)
        return None

    return backtrack(start)

def solve_with_bruteforce(matrix):
    start = State(matrix, bridges={}, cost=0)
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()
        if current.is_goal():
            return current.to_output_matrix()
        bridges_tuple = tuple(sorted(current.bridges.items()))
        if bridges_tuple in visited:
            continue
        visited.add(bridges_tuple)
        for neighbor in current.get_neighbors():
            stack.append(neighbor)
    return None
