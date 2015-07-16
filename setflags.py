import sys

def set_flags():
    """ Sets the various flags specified by a user """
    #if no file
    if len(sys.argv) == 1:
        print "You need to specifiy a file to read!"
        quit()

    out = sys.argv[2]
    cat = sys.argv[3]

    #debug?
    if "d" in sys.argv or "debug" in sys.argv:
        textout = True
    else:
        textout = False

    if "h" in sys.argv or "help" in sys.argv:
        help = True
    else:
        help = False

    if "-p" in sys.argv:
        print "get index of -p then add one for the parameter file"

    #aa or ua
    if "aa" in sys.argv:
        aa = True
    else:
        aa = False

    return textout,aa,out,cat,help
