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

import opls as op
import oplsatom
import oplsbond
import oplsangle
import oplsmolecule
import oplsdihedral

import babel
import write_nwchem

textout,aa,outname,lammpsin,help,isfile,fname = setflags.set_flags()
dataname = outname.split('/')
dataname = dataname[len(dataname)-1]
lammpsinput = lammpsin.split('/')
lammpsinput = lammpsin.split('.')
lammpsinput = lammpsinput[len(lammpsinput)-1]

if help:
    setparams.set_help(lammpsin,dataname)

if isfile:
    setparams.change_data_from_filein(fname,dataname)

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
#baddihedrals = dihedral.create_dihedrals(angles,True)
dihedral.set_dft(dihedrals,bonds)
rings = ring.create_rings(dihedrals)
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
molecule = molecule.create_molecule(atoms,bonds,angles,dihedrals,rings,fused_rings)

babel.read_babel_set('molecule/smdppeh.cml',atoms)

#print everything to text output as specified by boolean. DEBUGGING OUTPUT
if textout:
    print "ran"
    #pctotal = 0
    #for i in range(len(atoms)):
    #    pctotal += float(atoms[i].opls_partial)
    #print pctotal
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
    #printer.print_opls_dihedrals(opls_dihedrals)

    #reprint for opls add
    #printer.print_atoms(atoms,True)
    #printer.print_bonds(bonds,True)
    #printer.print_angles(angles,True)
    printer.print_dihedrals(dihedrals)
    printer.print_all_dft(dihedrals)
    #op.count_atoms(opls_atoms,atoms)

lammps = open(outname,"w")
sys.stdout = lammps

#writes out to lammps, this really should be done in a method, but it takes a assload of inputs
print "Written by CMLParser\n"
print "\t%s atoms" % len(atoms)
print "\t%s bonds" % len(bonds)
print "\t%s angles" % len(angles)
print "\t%s dihedrals\n" % len(dihedrals)
print "\t%s atom types" % len(unique_a)
print "\t%s bond types" % len(unique_b)
print "\t%s angle types" % len(unique_ang)
print "\t%s dihedral types\n" % len(unique_d)
print "\t%s %s xlo xhi" % (xmin,xmax)
print "\t%s %s ylo yhi" % (ymin,ymax)
print "\t%s %s zlo zhi\n" % (zmin,zmax)
print "Masses\n"
for i in range(len(unique_a)):
    print "%s %s" % (i+1,unique_a[i].opls_mass)
print "\nBond Coeffs\n"
for i in range(len(unique_b)):
    print "%s %s %s" % (i+1,unique_b[i].bond_force_const,unique_b[i].bond_equib_len)
print "\nAngle Coeffs\n"
for i in range(len(unique_ang)):
    print "%s %s %s" % (i+1,unique_ang[i].Angle_force_const,unique_ang[i].Angle_equib_len)
print "\nDihedral Coeffs\n"
for i in range(len(unique_d)):
    print "%s %s %s %s %s" % (i+1,unique_d[i].k1,unique_d[i].k2,unique_d[i].k3,unique_d[i].k4)
print "\nPair Coeffs\n"
for i in range(len(unique_a)):
    print "%s %s %s" % (i+1,unique_a[i].opls_epsilon,unique_a[i].opls_sigma)
print "\nAtoms\n"
for i in range(len(atoms)):
    if atoms[i].print_type == 0:
        atoms[i].print_type = 6
    print "%s 1 %s %s %s %s %s" % (i+1,atoms[i].print_type,atoms[i].opls_partial,atoms[i].x_pos,atoms[i].y_pos,atoms[i].z_pos)
#    print "%s 1 %s %s %s %s" % (i+1,atoms[i].print_type,atoms[i].x_pos,atoms[i].y_pos,atoms[i].z_pos)
print "\nBonds\n"
for i in range(len(bonds)):
    if bonds[i].print_type == 0:
        bonds[i].print_type = 6
    print "%s %s %s %s" % (i+1,bonds[i].print_type,bonds[i].bond_master.atom_id,bonds[i].bond_slave.atom_id)
print "\nAngles\n"
for i in range(len(angles)):
    print "%s %s %s %s %s" % (i+1,angles[i].print_type,angles[i].Angle_master.atom_id,angles[i].Angle_slave1.atom_id,angles[i].Angle_slave2.atom_id)
print "\nDihedrals\n"
for i in range(len(dihedrals)):
    #hack smdppeh specific TODO
    if dihedrals[i].print_type == 0:
        dihedrals[i].print_type = 8
    print "%s %s %s %s %s %s" % (i+1,dihedrals[i].print_type,dihedrals[i].dihedral_master1.atom_id,dihedrals[i].dihedral_master2.atom_id,dihedrals[i].dihedral_slave1.atom_id,dihedrals[i].dihedral_slave2.atom_id)
print ""
for i in range(len(atoms)):
    print "set atom %s diameter %s" % (i+1,atoms[i].opls_sigma)
lammps.close()

#writes input file for lammps to run
if help == False:
    lammps2 = open(lammpsin,"w")
    sys.stdout = lammps2

    print "# created by CMLParser\n"
    print "units real"
    print "atom_style full"
    print "boundary p p p"
    print "bond_style harmonic"
    print "dielectric 9.8"
    print "pair_style lj/cut/coul/long 20.0"
    print "angle_style harmonic"
    print "dihedral_style opls"
    print "special_bonds lj 0 1 1"
    print "improper_style none"
    print "kspace_style ewald 10"
    print "read_data %s" % dataname
    print "thermo_style custom step temp press ke pe etotal density"
    print "dump 1 all custom 200 %s.lammpstrj id type mol xs ys zs vx vy vz" % lammpsinput
    print "neighbor 10.0 bin"
    print "neigh_modify every 1 delay 0 one 10000"
    print "fix 1 all npt temp 100 100 100 iso 0.0 1 1000 drag 2"
    print "fix 2 all momentum 1 linear 1 1 1"
    print "velocity all create 100.00000 1223"
    print "timestep 1"
    print "thermo 100"
    print "run 10000"
    print "unfix 1"
    print "unfix 2"
    print "write_restart restart.%s\n\n" % lammpsinput
    print "replicate 10 10 10"
    print "undump 1"
    print "fix 1 all npt temp 100 300 100 iso 10 1 1000 drag 2"
    print "fix 2 all momentum 1 linear 1 1 1"
    print "velocity all create 100.00000 1223"
    print "dump 2 all custom 1000 %s.lammpstrj id type mol xs ys zs vx vy vz" % ("%s_final" % lammpsinput)
    print "run 500000"
    print "write_restart restart.%s" % ("%s_final" % lammpsinput)
    print "unfix 1"
    print "unfix 2"

    lammps2.close()

write_nwchem.dft(dihedrals)

os.chdir('outputs')
cometrun = open('run_%s' % lammpsinput,'w')
sys.stdout = cometrun

print "#!/bin/bash"
print '#SBATCH --job-name="cmlparser_run"'
print '#SBATCH --output="job.%j.%N.out"'
print '#SBATCH --partition=compute'

print '#SBATCH --nodes=2'
print '#SBATCH --ntasks-per-node=24'

print '#SBATCH -t 2:00:00'

print '#SBATCH -A sds154'

print 'module load python lammps'

print 'cd /oasis/scratch/comet/cjpais/temp_project/cmlparser_py/outputs'
print 'export OMP_NUM_THREADS=1'

print 'ibrun -np 48 lammps < in.rewriteout'

os.system('squeue run_%s' % lammpsinput)
