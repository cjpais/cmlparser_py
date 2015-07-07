import sys
import xml.etree.ElementTree as ET
import printer
import setflags

import atom
import bond
import angle
import dihedral
import ring
import fused

textout,aa = setflags.set_flags()

#import the cml file and read
cmlfile = sys.argv[1]
tree = ET.parse(cmlfile)
root = tree.getroot()

#create the list of atoms and bonds from the cml file
atomTree = root.findall('./atomArray/atom')
bondTree = root.findall('./bondArray/bond')

#create all the objects
atoms = atom.create_atoms(atomTree)
bonds = bond.create_bonds(bondTree,atoms)
angles = angle.create_angles(atoms,bonds)
dihedrals = dihedral.create_dihedrals(angles)
rings = ring.create_rings(dihedrals)
fused_rings = fused.create_fused_rings(rings)










#print everything to text output as specified by boolean
if textout:
    printer.print_atoms(atoms)
    printer.print_bonds(bonds)
    printer.print_angles(angles)
    printer.print_dihedrals(dihedrals)
    printer.print_ring(rings)
    printer.print_fused(fused_rings)
