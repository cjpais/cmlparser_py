"""
Created on Thurs May 21 22:23:22 2015

@author: Christopher Pais
"""

import sys
import xml.etree.ElementTree as ET
import helper as help

#get filename from commandline
file = sys.argv[1]
atoms = []
atom = []
bonds = []
bond = []

#create Atom object
class Atom(object):
    atom_id = ""
    atom_type = ""
    x_pos = 0.000
    y_pos = 0.000
    z_pos = 0.000
    Num_Bonds = 0
    Bonds = []

    #constructor
    def __init__(self, atom_id, atom_type, x_pos, y_pos, z_pos):
        self.atom_id = atom_id
        self.atom_type = atom_type
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos
    
    def Add_Bond(bond):
        if bond.bond_master == atom.atom_id:
            self.Bonds[Num_bonds] = bond.bond_slave 
            self.Num_Bonds += 1
        else if bond.bond_slave == atom.atom_id:
            self.Bonds[Num_bonds] = bond.bond_master
            self.Num_Bonds +=1
        else 
            sys.exit("Error: atom id does not match bonding atoms")
            
        

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

class Angle(object):
    Angle_type = ""
    Angle_master = ""
    Angle_slave1 = ""
    Angle_slave2 = ""
    
    def __init__(self, Angle_type, Angle_master, Angle_slave1, Angle_slave2):
        self.Angle_type = Angle_type
        self.Angle_master = Angle_master
        self.Angle_slave1 = Angle_slave1
        self.Angle_slave2 = Angle_slave2


def Find_Angles( atom, bond):
    Angles= []
    for j in range(0, len(atom):
        for i in range(0,len(bond))
            if bond[i].bond_master == atom[j].atom_id or bond[i].bond_slave == atom[j].atom_id:
                atom[j].Add_Bond[i] 
    a = 0 
    for j in range(0, len(atom)):
        if atom[j].Num_Bonds == 2:
            Angle_type = 1 # Need to change this to allow for different angle types
            Angles[a] = [ Angle_type, atom.Bonds[0], atom.atom_id, atom.Bonds[1]]
            a+=1
        if atom[j].Num_bonds == 3:
            Angle_type = 1 # Need to change..
            Angles[a] = [Angle_type, atom.Bonds[0], atom.atom_id, atom.Bonds[2]]
            a+=1 
            Angles[a] = [ Angle_type, atom.Bonds[0], atom.atom_id, atom.Bonds[1]]
            a+=1
        if atom[j].Num_bonds == 4:
            Angle_type = 1
            Angles[a] = [ Angle_type, atom.Bonds[0], atom.atom_id, atom.Bonds[1]]
            a+= 1
            Angles[a] = [Angle_type, atom.Bonds[0], atom.atom_id, atom.Bonds[2]]
            a+=1 
            Angles[a] = [Angle_type, atom.Bonds[0], atom.atom_id, atom.Bonds[3]
            a+=1
    return Angles
            
                
                    

#begin parsing, gets single atom. do in method
tree = ET.parse(file)
root = tree.getroot()
atomList = root.findall('./atomArray/atom')
bondList = root.findall('./bondArray/bond')

#create a bunch of atoms objects
for i in range(0, len(atomList)):
   atoms.append(help.get_atoms(atomList,i))
   aList = help.object_list(atoms[i])
   atom.append(Atom(aList[0],aList[1],aList[2],aList[3],aList[4]))

print "   ATOMS   "
print "-----------"
for k in range(0, len(atom)):
   print "Atom id: %s" % atom[k].atom_id
   print "Atom type: %s" % atom[k].atom_type
   print "X position: %s" % atom[k].x_pos
   print "Y position: %s" % atom[k].y_pos
   print "Z position: %s" % atom[k].z_pos
   print ""

#create a bunch of bond objects
for j in range(0, len(bondList)):
   bonds.append(help.get_atoms(bondList,j))
   bList = help.bond_list(bonds[j])
   bond.append(Bond(bList[0],bList[1],bList[2]))

print "   BONDS   "
print "-----------"
for z in range(0, len(bond)):
   print "Bond Type: %s" % bond[z].bond_type
   print "Bond Master(bonded from): %s" % bond[z].bond_master
   print "Bond Slave(bonded to): %s" % bond[z].bond_slave
   print ""

Angle_List = Find_Angles(atom, bond)
angle = []

for j in range(0, len(Angle_List)):
    angle.append(Angle(Angle_List[0], Angle_List[1], Angle_List[2], Angle_List[3]))
    
for i in range(0, len(angle)):
    print angle.Angle_Type, angle.Angle_master, angle.Angle_slave1, angle.Angle_slave2
    
