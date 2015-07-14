def get_molecule(atom,opls):
    for i in range(0,len(atom)):
        assign_h(atom[i],opls)
        is10(atom[i],opls)
        is13(atom[i],opls)
        is15(atom[i],opls)
        is17(atom[i],opls)
        is26(atom[i],opls)
        is90(atom[i],opls)
        is177(atom[i],opls)
        is178(atom[i],opls)
        is181(atom[i],opls)

def assign_atom_vars(atom,number,opls):
    atom.opls_id = opls[number].opls_id
    atom.opls_sigma = opls[number].sigma
    atom.opls_epsilon = opls[number].epsilon
    atom.opls_partial = opls[number].pc
    atom.opls_bondid = opls[number].opls_bondid
    atom.opls_mass = opls[number].amass

def gen_bondlist(atom):
    bondlist = []
    for i in range(0,atom.numbonds):
        bondlist.append(atom.atom_bonds[i].atom_type)
    return bondlist

def assign_h(atom,opls):
    if atom.atom_type == "H" and atom.numbonds == 1:
        bondlist = atom.atom_bonds
        if bondlist[0].opls_id == "80":
            assign_atom_vars(atom,84,opls)
        elif bondlist[0].opls_id == "81":
            assign_atom_vars(atom,84,opls)
        elif bondlist[0].opls_id == "90":
            assign_atom_vars(atom,90,opls)

def is10(atom,opls): #this is really a 80
    number = 79
    if atom.atom_type == "C" and atom.numbonds == 4:
        bondlist = gen_bondlist(atom)
        if "C" in bondlist:
            bondlist.remove("C")
            if "H" in bondlist:
                bondlist.remove("H")
                if "H" in bondlist:
                    bondlist.remove("H")
                    if "H" in bondlist:
                        assign_atom_vars(atom,number,opls)

def is13(atom,opls): # this is really 81
    number = 80
    if atom.atom_type == "C" and atom.numbonds == 4:
        bondList = gen_bondlist(atom)
        if "H" in bondList:
            bondList.remove("H")
            if "H" in bondList:
                bondList.remove("H")
                if "C" in bondList:
                    bondList.remove("C")
                    if "N" in bondList or "C" in bondList:
                        assign_atom_vars(atom,number,opls)

def is15(atom,opls):
    number = 14
    if atom.atom_type == "C" and atom.numbonds == 4:
        bondList = gen_bondlist(atom)
        if "C" in bondList:
            bondList.remove("C")
            if "C" in bondList:
                bondList.remove("C")
                if "C" in bondList and "H" in bondList:
                    assign_atom_vars(atom,number,opls)

def is17(atom,opls): #this is really a 90
    number = 89
    if atom.atom_type == "C" and atom.numbonds == 3:
        bondList = gen_bondlist(atom)
        if "C" in bondList:
            bondList.remove("C")
            if "C" in bondList and "H" in bondList:
                assign_atom_vars(atom,number,opls)

def is26(atom,opls):
    number = 25
    if atom.atom_type == "S" and atom.numbonds == 2:
        if atom.atom_bonds[0].atom_type == "C" and atom.atom_bonds[1].atom_type == "C":
            assign_atom_vars(atom,number,opls)

def is90(atom,opls):
    number = 89
    if atom.atom_type == "C" and atom.numbonds == 3:
        bondList = gen_bondlist(atom)
        if "C" in bondList:
            bondList.remove("C")
            if "C" in bondList:
                bondList.remove("C")
                if "C" in bondList or "S" in bondList or "N" in bondList:
                    assign_atom_vars(atom,number,opls)

def is177(atom,opls):
    number = 176
    if atom.atom_type == "C" and atom.numbonds == 3:
        bondList = gen_bondlist(atom)
        if "C" in bondList and "N" in bondList and "O" in bondList:
            assign_atom_vars(atom,number,opls)

def is178(atom,opls):
    number = 177
    if atom.atom_type == "O" and atom.numbonds == 1:
        if atom.atom_bonds[0].atom_type == "C":
            assign_atom_vars(atom,number,opls)

def is181(atom,opls):
    number = 180
    if atom.atom_type == "N" and atom.numbonds == 3:
        if atom.atom_bonds[0].atom_type == "C" and atom.atom_bonds[1].atom_type == "C" and atom.atom_bonds[2].atom_type == "C":
            assign_atom_vars(atom,number,opls)
