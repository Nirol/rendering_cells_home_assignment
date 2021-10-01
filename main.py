import sys

from utils.init_logic_utils import init_state
from utils.io_utils import read_input_file, parse_file_input, print_menu, process_user_input

if __name__ == '__main__':
    # read initial file
    file_input = read_input_file(sys.argv[1])
    cells = parse_file_input(file_input)
    init_state(cells)

    while(True):
        print_menu()
        user_input = input()
        process_user_input(user_input)