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

# TODO: Maybe move print statements to here?!
