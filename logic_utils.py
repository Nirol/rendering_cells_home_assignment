from typing import List
import networkx as nx
from cell_state import state
import re
from no_precedence_eval import no_precedence_eval, parse


def _parse_cell_in_equation(raw_cell)->str:
    '''parse a re match object representing a cell in an equation into
    the cell index'''
    cell_index = int(raw_cell.group(0)[1:-1])
    return str(state.cell_values[cell_index])

def evaluate_clean_equation(equation: str)->float:
    return no_precedence_eval(*parse(equation))


def find_equation_value(equation:str)->float:
    clean_equation = re.sub(r'{[0-9]+}', _parse_cell_in_equation, equation)
    return evaluate_clean_equation(clean_equation)


def evaluate_cell(cell_index: int) -> float:
    cell = state.cells[cell_index]
    if type(cell) == str:
        # cell is an equation, remove the '=' prefix and calculate equation
        equation_val = find_equation_value(cell[1:])
        return equation_val
    else:
        # cell is a number
        return cell


def find_cells_order() -> List[int]:
    '''compute an order for cell value computation based on the cell dependencies, using topological sort'''

    # create graph for topological sort
    G = nx.DiGraph()
    G.add_nodes_from(range(len(state.cells)))

    # for every cell (index) add an edge based on its dependencies.
    for index, index_dependencies in enumerate(state.dependencies):
        for index_dependencies in index_dependencies:
            G.add_edge(index_dependencies, index)

    ts = nx.topological_sort(G)
    return list(ts)


def find_equation_dependencies(equation:str)->List[int]:
    matches = re.finditer('{[0-9]+}', equation)
    equation_dependencies = []
    for i in matches:
        # remove {} wrapping the list index, and convert the result string into int:
        state_idx = int(i.group(0)[1:-1])
        equation_dependencies.append(state_idx)

    return equation_dependencies


def fill_cell_dependencies(state: list) -> List[List[int]]:
    dependencies = []
    for idx,cell in enumerate(state):
        if type(cell) == str:
            dependencies.append(find_equation_dependencies(cell))
        else:
            dependencies.append([])
    return dependencies