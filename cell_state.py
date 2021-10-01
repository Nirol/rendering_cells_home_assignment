from typing import List


class CellState:
    def __init__(self, cells: List=None, dependencies: List[List[int]]=None):
        self.cells = cells
        self.dependencies = dependencies
        self.cell_values = {}


    def compute_cell_values(self) -> None:
        '''Compute all cells values based on a legal order and save them inside the
        state cell_values dictionary'''
        from logic_utils import find_cells_order, evaluate_cell
        cells_order = find_cells_order()
        for cell_index in cells_order:
            self.cell_values[cell_index] = evaluate_cell(cell_index)


    def print_cell_values(self)-> None:
        cell_to_string_list = [f"[{idx}: {self.cell_values[idx]}], " for idx in range(len(self.cells))]
        cell_to_string =''.join(cell_to_string_list)
        print(cell_to_string[:-2])

    def __str__(self):
        return f'cells: {self.cells} \ndependencies: {self.dependencies}\nvalues: {self.cell_values}'


# global state variable
state: CellState = CellState()