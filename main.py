import sys

from cell_state import state
from utils import read_input_file, parse_file_input, print_menu, process_user_input

if __name__ == '__main__':
    # read initial file
    file_input = read_input_file(sys.argv[1])
    parse_file_input(file_input)

    while(True):
        print_menu()
        user_input = input()
        process_user_input(user_input)
