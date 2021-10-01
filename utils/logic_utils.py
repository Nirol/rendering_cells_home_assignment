from typing import List
import networkx as nx
from cell_state import state
import re
from utils.no_precedence_eval import no_precedence_eval, parse

def is_value_equation(value:str)->bool:
    return value[0] == '='

def _parse_cell_in_equation(raw_cell)->str:
    '''parse a re match object representing a cell in an equation into
    the cell index'''
    cell_index = int(raw_cell.group(0)[1:-1])
    return str(state.cell_values[cell_index])

def evaluate_clean_equation(equation: str)->float:
    '''evaluate an equation using a no precedence calculation'''
    return no_precedence_eval(*parse(equation))


def find_equation_value(equation:str)->float:
    '''solve a raw equation'''
    #start by changing cell references to the corresponding cell values
    clean_equation = re.sub(r'{[0-9]+}', _parse_cell_in_equation, equation)

    #evaluate a clean math equation (not containing cell references but only values)
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




def update_cell_dependencies(cell_index: int, cell_value, is_cell_equation:bool) -> None:
    if is_cell_equation:
        state.dependencies[cell_index] =  find_equation_dependencies(equation=cell_value)
    else:
        state.dependencies[cell_index] = []


def update_cell(cell_index, value, is_equation):
    '''upon single cell value change (option b), update the cell raw value, dependencies, and actual value '''
    state.cells[cell_index] = value
    update_cell_dependencies(cell_index=cell_index, cell_value=value, is_cell_equation=is_equation)
    state.cell_values[cell_index] = evaluate_cell(cell_index)

def find_dependent_cells(cell_index):
    '''find all the cells dependent on cell_index'''

    # A cell directly dependent on cell_index can be dependent on by other cells and so on
    dependent_on = [cell_index]
    dependent_cells = []
    while dependent_on:
        next_cell = dependent_on.pop()
        for idx,cell_dependencies_list in enumerate(state.dependencies):
            if next_cell in cell_dependencies_list:
                dependent_cells.append(idx)
                dependent_on.append(idx)
    return dependent_cells


def update_dependent_cells(cell_index):
    '''upon single cell value change (option b), update all the cells dependant on the changed cell '''

    # find all the cells dependent on cell_index
    cells_to_re_eval = find_dependent_cells(cell_index=cell_index)

    #make sure to re evaluate the dependent cell based on a correct order:
    cells_order = find_cells_order()
    cells_to_re_eval_ordered = [x for x in cells_order if x in cells_to_re_eval]


    for cell_to_re_eval in cells_to_re_eval_ordered:
        state.cell_values[cell_to_re_eval] = evaluate_cell(cell_to_re_eval)





