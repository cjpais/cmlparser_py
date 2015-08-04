import sys
import os
import xml.etree.ElementTree as ET
import printer
import setflags
import setparams

import atom
import bond
import angle
import dihedral
import ring
import fused
import molecule
import monomer

import opls as op
import oplsatom
import oplsbond
import oplsangle
import oplsmolecule
import oplsdihedral

import babel
import write_nwchem
import write_qchem

import tester

os.system('clear')

#set basic data names and get flags
moleculeboo,mname,dname,inname,debug,isfile,fname,help = setflags.set_flags_new()

# split names for ease later on
dataname = dname.split('/')
dataname = dataname[len(dataname)-1]
lammpsinput = inname.split('/')
lammpsinput = inname.split('.')
lammpsinput = lammpsinput[len(lammpsinput)-1]

if help:
    setparams.set_help(lammpsin,dataname)
if isfile:
    setparams.change_data_from_filein(fname,dataname)

#import the cml file and read
tree = ET.parse(mname)
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
#baddihedrals = dihedral.create_dihedrals(angles,True)
dihedral.set_dft(dihedrals,bonds)

print "Warning: The create_rings module is running, this may take a while"
rings = ring.create_rings(dihedrals,bonds)
print "Rings finished running"
fused_rings = fused.create_fused_rings(rings)

#get important OPLS info
opatom,van,partial,opbond,opangle,optorsion = op.getImportant(oplsfinal)

#deal with OPLS
opls_atoms = oplsatom.create_atoms(opatom,van,partial)
opls_bonds = oplsbond.create_bonds(opbond)
opls_angles = oplsangle.create_angles(opangle)
opls_dihedrals = oplsdihedral.create_dihedrals(optorsion)

#more OPLS fun
oplsmolecule.get_molecule(atoms,opls_atoms)
bond.set_opls(bonds,opls_bonds)
angle.set_opls(angles,opls_angles)
dihedral.set_opls(dihedrals,opls_dihedrals)

#unique types
unique_a = atom.uniq_types(atoms)
unique_b = bond.uniq_types(bonds)
unique_ang = angle.uniq_types(angles)
unique_d = dihedral.uniq_types(dihedrals)

#get type
atom.get_type(atoms,unique_a)
bond.get_type(bonds,unique_b)
angle.get_type(angles,unique_ang)
dihedral.get_type(dihedrals,unique_d)

#box size
xmin,ymin,zmin,xmax,ymax,zmax = atom.periodic_b_size(atoms)

#create Molecule object

sys.stdout = sys.__stdout__
#monomer handling
if moleculeboo:
    molecule1 = molecule.create_molecule(atoms,bonds,angles,dihedrals,rings,fused_rings)
elif moleculeboo == False:
    monomer1 = monomer.create_monomer(atoms,bonds,angles,dihedrals,rings,fused_rings)
    thorings = monomer.mark_thio(monomer1)
    intermono = monomer.find_intermono(monomer1)
    monomer.get_single_alist(monomer1)
    monomer.find_attach(monomer1)

#create babel and read to get better partials
babel.read_babel_set(mname,atoms)

#write different dft finders
#write_nwchem.dft(dihedrals)
write_qchem.write(atoms,dihedrals)
sys.stdout = sys.__stdout__

if debug:
    printer.debug(atoms,bonds,angles,dihedrals,rings,fused_rings,opls_atoms,opls_bonds,opls_angles,opls_dihedrals)

#print all the output files
printer.print_data(dname,atoms,bonds,angles,dihedrals,unique_a,unique_b,unique_ang,unique_d,xmin,xmax,ymin,ymax,zmin,zmax)
if help == False or isfile == False:
    printer.print_lammpsin(inname,dataname,lammpsinput)
sys.stdout = sys.__stdout__
printer.print_srun(lammpsinput)

#autorun
#os.system('sbatch run_%s' % lammpsinput)
