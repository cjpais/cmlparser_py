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
opatom,van,partial,opbond,angle = op.getImportant(oplsfinal)

#deal with OPLS
opls_atoms = oplsatom.create_atoms(opatom,van,partial)
opls_bonds = oplsbond.create_bonds(opbond)
opls_angles = oplsangle.create_angles(angle)

#more OPLS fun
oplsmolecule.get_molecule(atoms,opls_atoms)

bond.set_opls(bonds,opls_bonds)

#unique types
unique_a = atom.uniq_types(atoms)
unique_b = bond.uniq_types(bonds)

#get type
atom.get_type(atoms,unique_a)
bond.get_type(bonds,unique_b)

#box size
xmin,ymin,zmin,xmax,ymax,zmax = atom.periodic_b_size(atoms)

#print everything to text output as specified by boolean
if textout:
    print "ran"
    #print basic info
    #printer.print_atoms(atoms)
    #printer.print_bonds(bonds)
    #printer.print_angles(angles)
    #printer.print_dihedrals(dihedrals)
    #printer.print_ring(rings)
    #printer.print_fused(fused_rings)

    #print opls info (not very useful)
    #printer.print_opls_atoms(opls_atoms)
    #printer.print_opls_bonds(opls_bonds)
    #printer.print_opls_angles(opls_angles)

    #reprint for opls add
    #printer.print_atoms(atoms,True)
    #printer.print_bonds(bonds,True)
    #op.count_atoms(opls_atoms,atoms)

lammps = open(outname,"w")
sys.stdout = lammps

print "Written by CMLParser\n"
print "\t%s atoms" % len(atoms)
print "\t%s bonds\n" % len(bonds)
print "\t%s atom types" % len(unique_a)
print "\t%s bond types\n" % len(unique_b)
print "\t%s %s xlo xhi" % (xmin,xmax)
print "\t%s %s ylo yhi" % (ymin,ymax)
print "\t%s %s zlo zhi\n" % (zmin,zmax)
print "Masses\n"
for i in range(len(unique_a)):
    print "%s %s" % (i+1,unique_a[i].opls_mass)
print "\nBond Coeffs\n"
for i in range(len(unique_b)):
    print "%s %s %s" % (i+1,unique_b[i].bond_force_const,unique_b[i].bond_equib_len)
print "\nPair Coeffs\n"
for i in range(len(unique_a)):
    print "%s %s %s" % (i+1,unique_a[i].opls_epsilon,unique_a[i].opls_sigma)
print "\nAtoms\n"
for i in range(len(atoms)):
    if atoms[i].print_type == 0:
        atoms[i].print_type = 6
    print "%s 1 %s %s %s %s" % (i+1,atoms[i].print_type,atoms[i].x_pos,atoms[i].y_pos,atoms[i].z_pos)
print "\nBonds\n"
for i in range(len(bonds)):
    if bonds[i].print_type == 0:
        bonds[i].print_type = 6
    print "%s %s %s %s" % (i+1,bonds[i].print_type,bonds[i].bond_master.atom_id,bonds[i].bond_slave.atom_id)
