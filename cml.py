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

import opls as op
import oplsatom
import oplsbond
import oplsangle
import oplsmolecule

textout,aa,outname = setflags.set_flags()

#import the cml file and read
cmlfile = sys.argv[1]
tree = ET.parse(cmlfile)
root = tree.getroot()

#get the oplsfile for later use
oplsname = 'oplsaa.prm.txt'
oplsfile = open(oplsname,'r')
oplslist = oplsfile.readlines()
oplslist2 = op.splitList(oplslist)
oplsfinal = [x for x in oplslist2 if x != []]

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

#get important OPLS info
opatom,van,partial,bond,angle = op.getImportant(oplsfinal)

#deal with OPLS
opls_atoms = oplsatom.create_atoms(opatom,van,partial)
opls_bonds = oplsbond.create_bonds(bond)
opls_angles = oplsangle.create_angles(angle)

#more OPLS fun
oplsmolecule.get_molecule(atoms,opls_atoms)

#unique types
unique_a = atom.uniq_types(atoms)
unique_b = bond.uniq_types(bonds)

#print everything to text output as specified by boolean
if textout:
    #print basic info
    printer.print_atoms(atoms)
    printer.print_bonds(bonds)
    printer.print_angles(angles)
    printer.print_dihedrals(dihedrals)
    printer.print_ring(rings)
    printer.print_fused(fused_rings)

    #print opls info (not very useful)
    #printer.print_opls_atoms(opls_atoms)
    #printer.print_opls_bonds(opls_bonds)
    #printer.print_opls_angles(opls_angles)

    #reprint for opls add
    printer.print_atoms(atoms,True)
    op.count_atoms(opls_atoms,atoms)

lammps = open(outname,"w")
sys.stdout = lammps

print "Written by CMLParser\n"
print "\t%s atoms" % len(atoms)
print "\t%s bonds" % len(bonds)
print ""
print "\t%s atom types" % len(unique_a)
print "\t%s bond types" % "something else"


