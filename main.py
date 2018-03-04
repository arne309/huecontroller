#!env python

import argparse
import hue
from json_storage import JsonStorage

def main(argv):
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("-s","--set", nargs=2, type=str, help="--set KEY VALUE")
    options = parser.parse_args(argv)
    print(options)

    storage = JsonStorage("config.json")
    

    if options.set:
        storage.set(options.set[0],options.set[1])
    





if __name__=="__main__":
    import sys
    argv = sys.argv[1:] if len(sys.argv)>1 else []
    main(argv)
else:
    argv=""
    main(argv.split("-s foo bar"))