from relaxation import relaxation_formula
from sys import argv

if __name__ == "__main__":
    readings = [0, 0, 0, 6, 0, 8, 0, 10, 0, 0, 3, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 1, 
            1, 0, 0]
    confidence_levels = [1, 0, 0, 0.8, 0, 0.8, 0, 0, 0, 0, 0.6, 0, 0, 0, 0, 0, 0.1, 0, 0, 0, 0, 1, 0.8, 
            0, 0, 0, 0, 0, 0.6, 1, 0, 0]
    if len(argv) > 1:
        if argv[1] == '-i':
            relaxation_formula(readings, confidence_levels, int(argv[2]))
        elif argv[1] == '-help':
            print("Usage: python relaxation_run.py\nNo arguments result in 40 iterations, "\
                    "\n-i <numer_of_iterations>"
                " for desired amount of iterations.\n If no change occur between the iterations"\
                " the iterations will be cancelled.")
        else: 
            print("Invalid command!\npython relaxation_run.py -help for help")
    elif len(argv) == 1:
            relaxation_formula(readings, confidence_levels)

