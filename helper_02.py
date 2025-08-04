from pysat.solvers import Solver
from helper_01 import generate_cnf

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
