import parse as p
import oplsparse

accAtoms = ["N","S"]

def get_molecule(atom,opls):
    #is1(atom,opls)
    #is2(atom,opls)
    #is3(atom,opls)
    #is4(atom,opls)
    #is5(atom,opls)
    #is6(atom,opls)
    #is7(atom,opls)
    #is8(atom,opls)
    #is9(atom,opls)
    is10(atom,opls)
    #is11atom,opls)
    #is12(atom,opls)
    is13(atom,opls)
    is15(atom,opls)
    is17(atom,opls)
    is26(atom,opls)
    is90(atom,opls)
    is177(atom,opls)
    is178(atom,opls)
    is181(atom,opls)
    
def is181(atom,opls):
    number = 180
    if atom.atom_type == "N":
        if atom.Num_Bonds == 3:
            if p.find_atom_by_id(atom.Atom_Bonds[0]).atom_type == "C" and p.find_atom_by_id(atom.Atom_Bonds[1]).atom_type == "C" and p.find_atom_by_id(atom.Atom_Bonds[2]).atom_type == "C":
                print "181"
                atom.id = opls[number].atom_id
                atom.sigma = opls[number].sigma
                atom.epsilon = opls[number].epsilon
                atom.partial_charge = opls[number].partial_charge
                return True
    return False

def is10(atom,opls):
    number = 9
    if atom.atom_type == "C":
        if atom.Num_Bonds == 4:
            bondList = [p.find_atom_by_id(atom.Atom_Bonds[0]),p.find_atom_by_id(atom.Atom_Bonds[1]),p.find_atom_by_id(atom.Atom_Bonds[2]),p.find_atom_by_id(atom.Atom_Bonds[3])]
            bondList.sort()
            if bondList[0].atom_type == "C" and bondList[1].atom_type == "H" and bondList[2].atom_type == "H" and bondList[3].atom_type == "H":
                print "10"
                atom.id = opls[number].atom_id
                atom.sigma = opls[number].sigma
                atom.epsilon = opls[number].epsilon
                atom.partial_charge = opls[number].partial_charge
                return True
    return False

def is13(atom,opls):
    number = 12
    if atom.atom_type == "C":
        if atom.Num_Bonds == 4:
            bondList = [p.find_atom_by_id(atom.Atom_Bonds[0]),p.find_atom_by_id(atom.Atom_Bonds[1]),p.find_atom_by_id(atom.Atom_Bonds[2]),p.find_atom_by_id(atom.Atom_Bonds[3])]
            bondList.sort()
            if bondList[0].atom_type == "C" and bondList[1].atom_type == "C" and bondList[2].atom_type == "H" and bondList[3].atom_type == "H":
                print "13"
                atom.id = opls[number].atom_id
                atom.sigma = opls[number].sigma
                atom.epsilon = opls[number].epsilon
                atom.partial_charge = opls[number].partial_charge
                return True
            elif bondList[0].atom_type == "N" and bondList[1].atom_type == "C" and bondList[2].atom_type == "H" and bondList[3].atom_type == "H":
                print "13"
                atom.id = opls[number].atom_id
                atom.sigma = opls[number].sigma
                atom.epsilon = opls[number].epsilon
                atom.partial_charge = opls[number].partial_charge
                return True

def is90(atom,opls):
    number = 89
    if atom.atom_type == "C":
        if atom.Num_Bonds == 3:
            bondList = [p.find_atom_by_id(atom.Atom_Bonds[0]).atom_type,p.find_atom_by_id(atom.Atom_Bonds[1]).atom_type,p.find_atom_by_id(atom.Atom_Bonds[2]).atom_type]
            if "C" in bondList:
                bondList.remove("C")
                if "C" in bondList:
                    bondList.remove("C")
                    if "C" in bondList:
                        atom.id = opls[number].atom_id
                        atom.sigma = opls[number].sigma
                        atom.epsilon = opls[number].epsilon
                        atom.partial_charge = opls[number].partial_charge
                        print "90"
                    elif "S" in bondList:
                        atom.id = opls[number].atom_id
                        atom.sigma = opls[number].sigma
                        atom.epsilon = opls[number].epsilon
                        atom.partial_charge = opls[number].partial_charge
                        print "90"
                    elif "N" in bondList:
                        print "90"
                        atom.id = opls[number].atom_id
                        atom.sigma = opls[number].sigma
                        atom.epsilon = opls[number].epsilon
                        atom.partial_charge = opls[number].partial_charge

def is17(atom,opls):
    number = 16
    if atom.atom_type == "C":
        if atom.Num_Bonds == 3:
            bondList = [p.find_atom_by_id(atom.Atom_Bonds[0]).atom_type,p.find_atom_by_id(atom.Atom_Bonds[1]).atom_type,p.find_atom_by_id(atom.Atom_Bonds[2]).atom_type]
            if "C" in bondList:
                bondList.remove("C")
                if "C" in bondList and "H" in bondList:
                    print "17"
                    atom.id = opls[number].atom_id
                    atom.sigma = opls[number].sigma
                    atom.epsilon = opls[number].epsilon
                    atom.partial_charge = opls[number].partial_charge

def is26(atom,opls):
    number = 25
    if atom.atom_type == "S" and atom.Num_Bonds == 2:
        if p.find_atom_by_id(atom.Atom_Bonds[0]).atom_type == "C" and p.find_atom_by_id(atom.Atom_Bonds[1]).atom_type == "C":
            print "26"
            atom.id = opls[number].atom_id
            atom.sigma = opls[number].sigma
            atom.epsilon = opls[number].epsilon
            atom.partial_charge = opls[number].partial_charge

def is177(atom,opls):
    number = 176
    if atom.atom_type == "C" and atom.Num_Bonds == 3:
        bondList = [p.find_atom_by_id(atom.Atom_Bonds[0]).atom_type,p.find_atom_by_id(atom.Atom_Bonds[1]).atom_type,p.find_atom_by_id(atom.Atom_Bonds[2]).atom_type]
        if "C" in bondList and "N" in bondList and "O" in bondList:
            print "177"
            atom.id = opls[number].atom_id
            atom.sigma = opls[number].sigma
            atom.epsilon = opls[number].epsilon
            atom.partial_charge = opls[number].partial_charge

def is178(atom,opls):
    number = 177
    if atom.atom_type == "O" and atom.Num_Bonds == 1:
        if p.find_atom_by_id(atom.Atom_Bonds[0]).atom_type == "C":
            atom.id = opls[number].atom_id
            atom.sigma = opls[number].sigma
            atom.epsilon = opls[number].epsilon
            atom.partial_charge = opls[number].partial_charge
            print "178"

def is15(atom,opls):
    number = 14
    if atom.atom_type == "C" and atom.Num_Bonds == 4:
        bondList = [p.find_atom_by_id(atom.Atom_Bonds[0]).atom_type,p.find_atom_by_id(atom.Atom_Bonds[1]).atom_type,p.find_atom_by_id(atom.Atom_Bonds[2]).atom_type,p.find_atom_by_id(atom.Atom_Bonds[3]).atom_type]
        if "C" in bondList:
            bondList.remove("C")
            if "C" in bondList:
                bondList.remove("C")
                if "C" in bondList and "H" in bondList:
                    atom.id = opls[number].atom_id
                    atom.sigma = opls[number].sigma
                    atom.epsilon = opls[number].epsilon
                    atom.partial_charge = opls[number].partial_charge
                    print "15"