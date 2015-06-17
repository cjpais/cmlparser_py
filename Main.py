import sys
import xml.etree.ElementTree as ET
import helper as help
import time
import parse as p

#get filename from commandline
file = sys.argv[1]

#begin parsing
tree = ET.parse(file)
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

#get the dihedrals and print them
dihedrals = p.find_dihedrals(AngleList)
p.print_dihedrals(dihedrals)

#get the rings and print them
ring = p.find_ring(dihedrals)
p.print_ring(ring)