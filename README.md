# rendering_cells_home_assignment

## Running Instructions
1. Make sure to install the 'networkx' package (possibly by using the requirements.txt file).
2. run the program by 

```
main.py inpt
```
where 'input' is the file holding the example parameter.

3. Note: Please insert the example as in the assignment file example // the current input file example, the program does not support
    any deviation from the format.
    
## Files

**Main Folder**
1. [main.py](main.py) - The main program run function, parsing the input and running the program user input loot.
2. [cell_state.py](cell_state.py) - Define the CellState class and the global object used by the program to save the current state.
3. [input](input) - The file holding the input.

**Utils**
1. [init_logic_utils.py](/utils/init_logic_utils.py) - hold logic util methods used upon program start to init the program state.
2. [logic_utils.py](/utils/logic_utils.py) - logic util methods used to calculate cells values and dependencies.
3. [io_utils.py](/utils/io_utils.py) - IO utils used to print info to the user or parse the user input.
4. [no_precedence_eval.py](/utils/no_precedence_eval.py) - simple implementation for no precedence equation evaluation from string to a number.



