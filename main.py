#!env python

import argparse
import hue

def main(argv):
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument(argv)



if __name__=="__main__":
    import sys
    main(sys.argv)
else:
    argv=""
    main(argv.split(" "))