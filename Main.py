import sys
import xml.etree.ElementTree as ET
import helper as help
import time
import parse as p

#get filename from commandline
file = sys.argv[1]
atoms = []
atom = []
bonds = []
bond = []
angle = []

#begin parsing, gets single atom. do in method
tree = ET.parse(file)
root = tree.getroot()
atomList = root.findall('./atomArray/atom')
bondList = root.findall('./bondArray/bond')

atom = p.create_atomobj(atomList)
bond = p.create_bondobj(bondList)

p.print_atoms(atom)
p.print_bonds(bond)

AngleList = p.print_find_angles(atom,bond)

dihedrals = p.find_dihedrals(AngleList)
p.print_dihedrals(dihedrals)