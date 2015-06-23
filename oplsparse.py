class OPLS_Atom(object):
    atom_id = ""
    atom_type = ""
    partial_charge = ""
    sigma = ""
    epsilon = ""

    #constructor
    def __init__(self, atom_id, atom_type, partial_charge, sigma, epsilon):
        self.atom_id = atom_id
        self.atom_type = atom_type
        self.partial_charge = partial_charge
        self.sigma = sigma
        self.epsilon = epsilon

def getAtoms(oplslist):
    atomList = []
    for i in range(0,len(oplslist)):
        curLine = oplslist[i]
        if curLine[0] == "atom":
            atomList.append(curLine)
    return atomList

def getVan(oplslist):
    vanList = []
    for i in range(0,len(oplslist)):
        curLine = oplslist[i]
        if curLine[0] == "vdw":
            vanList.append(curLine)
    return vanList

def getPartial(oplslist):
    partialList = []
    for i in range(0,len(oplslist)):
        curLine = oplslist[i]
        if curLine[0] == "charge":
            partialList.append(curLine)
    return partialList

def splitList(oplslist):
    bigList = []
    for i in range(0,len(oplslist)):
        split = oplslist[i].split()
        bigList.append(split)
    return bigList

def create_opls_atom(atom,van,partial):
    opls_atoms = []
    for i in range(0,len(atom)):
        aList =  atom[i]
        vList = van[i]
        pList = partial[i]
        opls_atoms.append(OPLS_Atom(aList[1],aList[3],pList[2],vList[2],vList[3]))
    return opls_atoms

def print_opls_atoms(opls_atoms):
    print "----------OPLS ATOMS----------"
    for i in range(0,len(opls_atoms)):
        print ""
        print opls_atoms[i].atom_type
        print opls_atoms[i].atom_id
        print opls_atoms[i].sigma
        print opls_atoms[i].epsilon
        print opls_atoms[i].partial_charge