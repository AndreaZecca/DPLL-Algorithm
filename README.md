# DPLL Algorithm
Implementation of DPLL algorithm for solving SAT problems.

## Usage
You can both run the script passing as parameter a file containing the formula or you can run the script and then type the formula in the terminal.
```
python dpll.py -f <input_file>
```
The formula must be in CNF form.\
E.g.:
```
(a or b) and (not a or not b)
```
An example of satisfiable formula has been provided in the file `SAT_formula.cnf`.\
An example of unsatisfiable formula has been provided in the file `UNSAT_formula.cnf`.