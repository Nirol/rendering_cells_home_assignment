def read_input_file(file_name):
    with open(file_name) as f:
        # Assuming the input file hold a single input line
        input_data = f.readline()
        return input_data

def parse_file_input(input: str)-> list:
    #TODO complete method
    return []

def print_menu()->None:
    option_a ="\t Print current state"
    option_b ="\t Change a value"
    print("\n".join(["Menu", option_a, option_b]))


def print_current_state()->None:
    #TODO complete method
    pass

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