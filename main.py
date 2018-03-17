#!env python

import argparse
import hue
from json_storage import JsonStorage
from pprint import pprint



def main(argv):
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("-s","--set", nargs=2, type=str, help="--set KEY VALUE")
    parser.add_argument("-l","--lights", action="store_true", dest="showlights", help="Show lights")
    parser.add_argument("-g","--groups", action="store_true", dest="showgroups", help="Show groups")
    parser.add_argument("-r","--rules", action="store_true", dest="showrules", help="Show rules")
    parser.add_argument("-w","--watch", action="store_true", dest="watch", help="Watch for changes")
    options = parser.parse_args(argv)
    print(options)

    storage = JsonStorage("config.json")
    
    
    try:
        h = hue.Hue(storage)
        if options.showlights: 
            pprint(h.getLights())
        
        if options.watch:
            h.watch(pprint)
        
        if options.showgroups:
            pprint(h.getGroups())

        if options.showrules:
            pprint(h.getRules())

    except Exception as e:
        print(e)
    





if __name__=="__main__":
    import sys
    argv = sys.argv[1:] if len(sys.argv)>1 else []
    main(argv)
else:
    argv=""
    main(argv.split("-s foo bar"))