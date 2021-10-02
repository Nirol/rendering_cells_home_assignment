from typing import List

from networkx import NetworkXUnfeasible

from cell_state import state
from utils.logic_utils import find_equation_dependencies, find_cells_order, evaluate_cell


def fill_cells_dependencies(cells: list) -> List[List[int]]:
    '''find all cells dependencies upon new program run'''
    dependencies = []
    for idx,cell in enumerate(cells):
        if type(cell) == str:
            dependencies.append(find_equation_dependencies(cell))
        else:
            dependencies.append([])
    return dependencies

def compute_cell_values() -> None:
    '''Compute all cells values based on a legal order and save them inside the
    state cell_values dictionary'''
    try:
        cells_order = find_cells_order()
    except NetworkXUnfeasible:
        print("Bad input cells received, dependency circulation found!")
        raise ValueError()
    for cell_index in cells_order:
        state.cell_values[cell_index] = evaluate_cell(cell_index)

def init_state(cells: List)->None:
    # find all cells dependencies
    dependencies = fill_cells_dependencies(cells=cells)

    #update the global state variable:
    state.cells = cells
    state.dependencies = dependencies
    compute_cell_values()