from typing import List
from cell_state import state
from logic_utils import fill_cell_dependencies


def read_input_file(file_name):
    with open(file_name) as f:
        # Assuming the input file hold a single input line
        input_data = f.readline()
        return input_data


def parse_file_input(input: str)-> None:
    input_list: List[str] = input.split(", ")
    cells =[]
    #convert all non equation into numeric values:
    for value in input_list:
        if value[0] != '=':
            cells.append(float(value))
        else:
            cells.append(value)

    # find all cells dependencies
    dependencies = fill_cell_dependencies(state=cells)

    #update the global state variable:
    state.cells = cells
    state.dependencies = dependencies


def print_menu()->None:
    option_a ="\t a.Print current state"
    option_b ="\t b.Change a value"
    print("\n".join(["Menu", option_a, option_b]))


def print_current_state()->None:
    state.compute_cell_values()
    state.print_cell_values()

def change_value(user_input: str):
    #TODO complete method
    pass

def process_user_input(user_input: str)->None:
    valid_options =['a','b']
    if user_input not in valid_options:
        print("Invalid user input")

    elif user_input == 'a':
        print_current_state()
    else:
        change_value(user_input)