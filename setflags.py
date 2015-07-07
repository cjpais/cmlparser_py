import sys

def set_flags():
    #if no file
    if len(sys.argv) == 1:
        print "You need to specifiy a file to read!"
        quit()

    #debug?
    if "d" in sys.argv or "debug" in sys.argv:
        textout = True
    else:
        textout = False

    #aa or ua
    if "aa" in sys.argv:
        aa = True
    else:
        aa = False

    return textout,aa
