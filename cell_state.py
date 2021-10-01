from typing import List

class CellState:
    def __init__(self, cells: List=None, dependencies: List[List[int]]=None):
        self.cells = cells
        self.dependencies = dependencies
        self.cell_values = {}


    def __str__(self):
        return f'cells: {self.cells} \ndependencies: {self.dependencies}\nvalues: {self.cell_values}'



# global state variable
state: CellState = CellState()