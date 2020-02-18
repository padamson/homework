#!/usr/bin/python

import sys, getopt


def value(outputfile):
    with open(outputfile, “w”) as f: 
        f.write(“Hello World”) 


def main(argv):
    prob_type = None
    outputfile = None
    try:
        opts, args = getopt.getopt(argv,"hp:o:",["ptype=", "ofile="])
    except getopt.GetoptError:
        print 'add_subtract.py -p <problem_type> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'add_subtract.py -p <proble_type> -o <outputfile>'
            sys.exit()
        elif opt in ("-p", "--ptype"):
            prob_type = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if not prob_type:
        prob_type = 'value'
    if not outputfile:
        outputfile = 'out.tex'

    print('Creating worksheet for problem type {} in {}.'.format('value', outputfile))

    if prob_type is 'value':
        value(outputfile)


if __name__ == "__main__":
    main(sys.argv[1:])
