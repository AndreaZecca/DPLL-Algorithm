import sys
import re
from argparse import ArgumentParser

def getfilename():
    arg = ArgumentParser()
    arg.add_argument("-f", "--file", help="File containing CNF formula")
    filename = arg.parse_args().file
    return filename

def dpll(clauses, augmented=False):
    X = clauses.copy()
    change = False
    while True:
        for clause in X:
            if len(clause) == 1:
                X = unit_resolution(clause[0], X)
                change = True    
        if not change:
            break
        change = False
    if len(X) == 0:
        return True
    else:
        if not augmented:
            new_literal = clauses[0][0]
            return dpll(clauses + [[f'not {new_literal}']], True) or dpll(clauses + [[new_literal]], True)


def unit_resolution(literal, X):
    is_negated = 'not' in literal
    for clause in X:
        if literal in clause:
            X.remove(clause)
        elif is_negated and literal.replace('not ', '') in clause:
            clause.remove(literal.replace('not ', ''))
        elif not is_negated and f'not {literal}' in clause:
            clause.remove(f'not {literal}')
    return X


def main():
    filename = getfilename()
    formula = ""
    if filename:
        try:
            f = open(filename, 'r')
            formula = ''.join(f.readlines()).replace('\n','').strip()
            f.close()
        except IOError:
            print("File not found")
            sys.exit(1)
    else:
        formula = input("Enter a formula in CNF: ")
    formula = formula.lower()
    # splitting formula into clauses based on the pharenthesis
    clauses = re.split(r'and', formula)
    clauses = [clause.replace('(','').replace(')','').strip().split(r' or ') for clause in clauses if clause != '']
    
    if len(clauses) == 0:
        print("No clauses found")
        sys.exit(1)

    sat = dpll(clauses)
    
    if sat:
        print(f"Formula is satisfiable")
    else:
        print("Formula is not satisfiable")
if __name__ == '__main__':
    main()