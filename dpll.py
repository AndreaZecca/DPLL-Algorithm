import sys
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
    
if __name__ == '__main__':
    main()