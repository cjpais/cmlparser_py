"""
Created on Thurs May 21 22:23:22 2015

@author: Christopher Pais
"""

import sys
import xml.etree.ElementTree as ET
import helper as help
import time

#get filename from commandline
file = sys.argv[1]
atoms = []
atom = []
bonds = []
bond = []
angle = []
start_time = time.time()

#create Atom object
class Atom(object):
    atom_id = ""
    atom_type = ""
    x_pos = 0.000
    y_pos = 0.000
    z_pos = 0.000
    Num_Bonds = 0
    Atom_Bonds = []
    primary = {}
    secondary = {}
    tertiary = {}
    related = {}
    ring = False

    #constructor
    def __init__(self, atom_id, atom_type, x_pos, y_pos, z_pos):
        self.atom_id = atom_id
        self.atom_type = atom_type
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos
        self.Atom_Bonds = []
        self.Num_Bonds = 0
        ring = False
        primary = {}
        secondary = {}
        tertiary = {}
        related = {}

#create Bond object 
class Bond(object):
   bond_type = ""
   bond_master = ""
   bond_slave = ""

   #constructor
   def __init__(self, bond_type, bond_master, bond_slave):
      self.bond_type = bond_type
      self.bond_master = bond_master
      self.bond_slave = bond_slave

#create angle object
class Angle(object):
    Angle_type = 0
    Angle_master = ""
    Angle_slave1 = ""
    Angle_slave2 = ""
    
    #constructor
    def __init__(self, Angle_type, Angle_master, Angle_slave1, Angle_slave2):
        self.Angle_type = Angle_type
        self.Angle_master = Angle_master
        self.Angle_slave1 = Angle_slave1
        self.Angle_slave2 = Angle_slave2 

def find_atom_by_id(checkId):
    for i in range(0, len(atom)):
        if atom[i].atom_id == checkId:
            return atom[i]
    else:
        print "no atom found by that id" 

def find_angles(atom, bondList):
    """
    Find the angles give an atoms and a list of bonds. Returns a list of angles

    Keyword Arguments:
    atom -- The specific atom to find the angles for
    bondList -- The list of bonds the atom might have
    """"
    
    Angles = []
    if atom.Num_Bonds > 1:
       for i in range(0, atom.Num_Bonds):
          ang_type = 1
          Angles.append(Angle(ang_type,atom.Bonds[0],atom.atom_id,atom.Bonds[i]))
       return Angles                    
          if atom.Bonds[0] != atom.Bonds[i]:
              Angles.append(Angle(ang_type,atom.Bonds[0],atom.atom_id,atom.Bonds[i]))
    return Angles

def getAtoms(atomList):
#create a bunch of atoms objects
for i in range(0, len(atomList)):
   atoms.append(help.get_atoms(atomList,i))
   aList = help.object_list(atoms[i])
   atom.append(Atom(aList[0],aList[1],aList[2],aList[3],aList[4]))

def getBondObj(bondList):
#create a bunch of bond objects
for j in range(0, len(bondList)):
   bonds.append(help.get_atoms(bondList,j))
   bList = help.bond_list(bonds[j])
   bond.append(Bond(bList[0],bList[1],bList[2]))

def printAtoms(atom)
# print the atoms
print "   ATOMS   "
print "-----------"
for k in range(0, len(atom)):
   print "Atom id: %s" % atom[k].atom_id
   print "Atom type: %s" % atom[k].atom_type
   print "X position: %s" % atom[k].x_pos
   print "Y position: %s" % atom[k].y_pos
   print "Z position: %s" % atom[k].z_pos
   print ""

# print the bonds
print "   BONDS   "
print "-----------"
for z in range(0, len(bond)):
   print "Bond Number %s" % z
   print "Bond Type: %s" % bond[z].bond_type
   print "Bond Master(bonded from): %s" % bond[z].bond_master
   print "Bond Slave(bonded to): %s" % bond[z].bond_slave
   print ""

# print the angles to (eventually) calculate
AngleList = []
print "   ANGLES   "
print "------------"
for i in range(0,len(atom)):
  help.get_num_bonds(atom[i],bond)
  angles = find_angles(atom[i],bond)
  if atom[i].Num_Bonds > 1:
    for x in range(0,len(angles)):
      AngleList.append(angles[x])
      print "Angle Type: %s" % angles[x].Angle_type
      print "Master Angle: %s" % angles[x].Angle_master
      print "Slave angle 1: %s" % angles[x].Angle_slave1
      print "Slave angle 2: %s" % angles[x].Angle_slave2
      print ""

#get dihedrals
print ""
dihedrals = []
for i in range(0,len(AngleList)):
    angleMaster = find_atom_by_id(AngleList[i].Angle_master)
    angleSlave1 = find_atom_by_id(AngleList[i].Angle_slave1)
    if angleMaster.atom_type == "H" or angleSlave1.atom_type == "H":
        continue
    fList = [AngleList[i].Angle_master,AngleList[i].Angle_slave1]
    fList.sort()
    for j in range(i, len(AngleList)):
        angleMaster2 = find_atom_by_id(AngleList[i].Angle_master)
        angleSlave2 = find_atom_by_id(AngleList[i].Angle_slave2)
        angleSlave12 = find_atom_by_id(AngleList[i].Angle_slave1)
        if angleMaster2.atom_type == "H" or angleSlave12.atom_type == "H" or angleSlave2.atom_type == "H":
            continue
        sList = [AngleList[j].Angle_slave1,AngleList[j].Angle_slave2]
        sList.sort()
        sList2 = [AngleList[j].Angle_master,AngleList[j].Angle_slave1]
        sList2.sort()
        if fList == sList2:
            dihedrals.append(AngleList[i])
        elif fList == sList:
            dihedrals.append(AngleList[i])
dihedrals = list(set(dihedrals))

for i in range(0,len(dihedrals)):
    print "Dihedral %s: %s" % (i,dihedrals[i])

#print the running time   
print("--- %s seconds ---" % (time.time() - start_time))