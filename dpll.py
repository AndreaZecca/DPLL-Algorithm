import sys
import re
from argparse import ArgumentParser

def getfilename():
    arg = ArgumentParser()
    arg.add_argument("-f", "--file", help="File containing CNF formula")
    filename = arg.parse_args().file
    return filename

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
    clauses = [clause for clause in clauses if clause != '']
    clauses = [clause.strip() for clause in clauses]
    clauses = [clause.replace('(','').replace(')','').strip().split(r' or ') for clause in clauses]

    print(formula)
    print(clauses)

if __name__ == '__main__':
    main()