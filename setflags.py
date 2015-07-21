import sys

def set_flags():
    """ Sets the various flags specified by a user """
    #if no file
    fname = ""

    if len(sys.argv) == 1:
        print "You need to specifiy a file to read!"
        quit()

    out = sys.argv[2]
    cat = sys.argv[3]

    if "-f" in sys.argv:
        isfile = True
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-f':
                index = i+1
        fname = sys.argv[index]
    else:
        isfile = False

    #debug?
    if "d" in sys.argv or "debug" in sys.argv:
        textout = True
    else:
        textout = False

    if "h" in sys.argv or "help" in sys.argv:
        help = True
    else:
        help = False

    #aa or ua
    if "aa" in sys.argv:
        aa = True
    else:
        aa = False

    return textout,aa,out,cat,help,isfile,fname
