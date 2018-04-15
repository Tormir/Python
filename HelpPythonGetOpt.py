#!/usr/bin/python3

import getopt, sys

def main():
    found_o = False
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            print("-o is required")
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
            found_o = True
        else:
            assert False, "wrong flag"
    if not found_o:
        print("-o was not given")
        sys.exit(2)

if __name__ == "__main__":
    main()
