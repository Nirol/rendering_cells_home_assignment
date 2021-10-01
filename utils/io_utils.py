from typing import List
from cell_state import state
from utils.logic_utils import update_cell, is_value_equation, update_dependent_cells


def read_input_file(file_name):
    with open(file_name) as f:
        # Assuming the input file hold a single input line
        input_data = f.readline()
        return input_data

def parse_file_input(input: str)-> List:
    input_list: List[str] = input.split(", ")
    cells =[]
    #convert all non equation into numeric values:
    for value in input_list:
        if is_value_equation(value):
            cells.append(value)
        else:
            cells.append(float(value))

    return cells

def print_menu()->None:
    option_a ="\t a.Print current state"
    option_b ="\t b.Change a value"
    print("\n".join(["Menu", option_a, option_b]))

def print_cell_values() -> None:
    cell_to_string_list = [f"[{idx}: {state.cell_values[idx]}], " for idx in range(len(state.cells))]
    cell_to_string = ''.join(cell_to_string_list)
    print(cell_to_string[:-2])

def print_current_state()->None:
    print_cell_values()

def change_value(user_input: str):
    input_list = user_input.split()
    cell_index = int(input_list[1])
    is_equation = is_value_equation(input_list[2])

    if is_equation:
        cell_value = input_list[2]
    else:
        cell_value = float(input_list[2])
    update_cell(cell_index=cell_index, value=cell_value, is_equation=is_equation)
    update_dependent_cells(cell_index=cell_index)




def process_user_input(user_input: str)->None:
    valid_options =['a','b']
    if not user_input or user_input[0] not in valid_options:
        print("Invalid user input")

    elif user_input == 'a':
        print_current_state()
    else:
        change_value(user_input)


