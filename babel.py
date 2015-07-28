import os

#TODO THIS FUCKING SHIT IS NOT GENERAL. JUST SMDPPEH. ALSO RENAME THE FUCKING LIST CALLED HI
def read_babel_set(filename,atom):
    os.system('babel -i cml molecules/smdppeh.cml -o mol2 molecules/smdppeh.mol2')
    bfile = open("molecules/smdppeh.mol2")
    blist = bfile.readlines()

    hi = []
    for i in range(len(blist)):
        split1 = blist[i].split()
        if blist[i] == "@<TRIPOS>ATOM\n":
            for j in range(i+1,len(blist)):
                if blist[j] == "@<TRIPOS>BOND\n":
                    break
                else:
                    split = blist[j].split()
                    hi.append(split[8])
    for i in range(len(atom)):
        atom[i].opls_partial = hi[i]
