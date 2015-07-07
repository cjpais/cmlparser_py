import oplsparse as op
import Queue

def count_atoms(opls_atoms,atoms):
    """ Counts the type of atoms found in the opls file for the molecule

        Keyword Arguments:
        opls_atoms - The list of Opls Atoms created in the oplsparse file
        atoms - The list of atoms that get values assigned to them and used throughout
    """
    for i in range(0,len(opls_atoms)):
        counter = 0
        for j in range(0,len(atoms)):
            if atoms[j].id == opls_atoms[i].atom_id:
                counter += 1
        if counter != 0:
            print "There are %s of opls_id #%s" % (counter,opls_atoms[i].atom_id)

def count_atom_type(atoms):
    """ Counts the number of different types of atoms for the molecule for 
        lammps output.

        Keyword Arguments:
        atoms - the list of atoms that get values assigned to them throughout the program
    """
    atom_types = []
    for j in range(0,len(atoms)):
        if atoms[j].id in atom_types:
            continue
        else:
            atom_types.append(atoms[j].id)
    if "" in atom_types:
        atom_types.remove("")
    return atom_types

def opls_bond_info(bonds):
    new = []
    for i in range(0,len(bonds)):
        if [bonds[i].bond_equib_len,bonds[i].bond_force_const] in new:
            continue
        elif [bonds[i].bond_equib_len,bonds[i].bond_force_const] == ['','']:
            continue
        else:
            new.append([bonds[i].bond_equib_len,bonds[i].bond_force_const])
    return new

def opls_angle_info(angle):
    new = []
    for i in range(0,len(angle)):
        if [angle[i].Angle_equib_len,angle[i].Angle_force_const] in new:
            continue
        elif [angle[i].Angle_equib_len,angle[i].Angle_force_const] == ['','']:
            continue
        else:
            new.append([angle[i].Angle_equib_len,angle[i].Angle_force_const])
    return new

"""
def count_angle_type(angles):
        Counts the number of different types of atoms for the molecule for 
        lammps output.

        Keyword Arguments:
        atoms - the list of atoms that get values assigned to them throughout the program
        
    atom_types = []
    for j in range(0,len(atoms)):
        if atoms[j].id in atom_types:
            continue
        else:
            atom_types.append(atoms[j].id)
    if "" in atom_types:
        atom_types.remove("")
    return atom_types    
"""

# TODO: Maybe move print statements to here?!
