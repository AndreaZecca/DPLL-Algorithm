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
    redo = True
    while redo:
        redo = False
        for clause in X:
            if len(clause) == 1:
                X = unit_resolution(clause[0], X)
                if "bot" in X:
                    return False
                redo = True   
                break 
    if len(X) == 0:
        return True
    else:
        if not augmented:
            new_literal = clauses[0][0]
            new_literal = new_literal.replace('not ', '')
            return dpll([[f'not {new_literal}']] + clauses, True) or dpll([[new_literal]] + clauses, True)
        else:
            return False


def unit_resolution(literal, X):
    is_negated = 'not' in literal
    new_X = []
    for clause in X:
        if literal in clause:
            if is_negated and literal.replace('not','') in clause:
                new_X.append("bot")
            elif not is_negated and f'not {literal}' in clause:
                new_X.append("bot")
            else:
                continue
        elif is_negated and literal.replace('not ', '') in clause:
            clause = [l for l in clause if l != literal.replace('not ', '')]
                # clause.remove(literal.replace('not ', ''))
            if len(clause) > 0:
                new_X.append(clause)
            else :
                new_X.append("bot")
        elif not is_negated and f'not {literal}' in clause:
            clause = [l for l in clause if l != f'not {literal}']
            # clause.remove(f'not {literal}')
            if len(clause) > 0:
                new_X.append(clause)
            else :
                new_X.append("bot")
        else:
            new_X.append(clause)
    return new_X


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