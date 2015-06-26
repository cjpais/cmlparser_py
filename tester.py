import oplsparse as op
import Queue

def count_atoms(opls_atoms,atoms):
    for i in range(0,len(opls_atoms)):
        counter = 0
        for j in range(0,len(atoms)):
            if atoms[j].id == opls_atoms[i].atom_id:
                counter += 1
        if counter != 0:
            print "There are %s of opls_id #%s" % (counter,opls_atoms[i].atom_id)

# TODO: Maybe move print statements to here?!
