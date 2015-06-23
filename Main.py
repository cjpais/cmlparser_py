import sys
import xml.etree.ElementTree as ET
import parse as p
import typeofmolecule as t
import oplsparse as op
import time

start = time.time()
twoArg = False

if len(sys.argv) > 2:
    print "ran"
    old_stdout = sys.stdout
    log_file = open(sys.argv[2],"w")
    sys.stdout = log_file

#get filename from commandline
cmlfile = sys.argv[1]

#begin parsing
tree = ET.parse(cmlfile)
root = tree.getroot()

atomList = root.findall('./atomArray/atom')
bondList = root.findall('./bondArray/bond')

#create a bunch of atom and bond objects
atom = p.create_atomobj(atomList)
bond = p.create_bondobj(bondList)

#print the atom and bond objects
p.print_atoms(atom)
p.print_bonds(bond)

#get a list of angles formed by the bonds
AngleList = p.print_find_angles(atom,bond)
p.print_angles(AngleList)

#get the dihedrals and print them
dihedrals = p.find_dihedrals(AngleList)
p.print_dihedrals(dihedrals)

#get the rings and print them
ring = p.find_ring(dihedrals)
p.print_ring(ring)

#get the fused rings and print them
#TODO
"""fused = p.find_fused(ring)
p.print_fused(fused)"""

#begin to parse the opls file
opls_file = 'oplsaa.prm.txt'
oplsfile = open(opls_file,'r')
oplslist = oplsfile.readlines()

oplsMatrix = op.splitList(oplslist)
oplsMatrix2 = [x for x in oplsMatrix if x != []]
opls_atom_ids = op.getAtoms(oplsMatrix2)
opls_van = op.getVan(oplsMatrix2)
opls_partial = op.getPartial(oplsMatrix2)

opls_atoms = op.create_opls_atom(opls_atom_ids,opls_van,opls_partial)
op.print_opls_atoms(opls_atoms)

for i in range(0,len(atom)):
    t.get_molecule(atom[i],opls_atoms)

p.print_atoms(atom)

print("--- %s seconds ---" % (time.time() - start))

if twoArg:
    sys.stdout = old_stdout
    log_file.close()