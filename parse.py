import sys
import xml.etree.ElementTree as ET
import helper as help
import time

atoms = []
atom = []
bonds = []
bond = []
angle = []
ignore_list = []

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

#create dihedral object
class Dihedral(object):
    #these are atoms not angles
    Angle_master1 = ""
    Angle_master2 = ""
    Angle_slave1 = ""
    Angle_slave2 = ""

    def __init__(self, Angle_master1, Angle_master2, Angle_slave1, Angle_slave2):
        self.Angle_master1 = Angle_master1
        self.Angle_master2 = Angle_master2
        self.Angle_slave1 = Angle_slave1
        self.Angle_slave2 = Angle_slave2

#create ring object
class Ring(object):
    ring_type = 0
    atom1 = ""
    atom2 = ""
    atom3 = ""
    atom4 = ""
    atom5 = ""
    atom6 = ""

    def __init__(self,a1,a2,a3,a4,a5,a6=None):
        self.atom1 = a1
        self.atom2 = a2
        self.atom3 = a3
        self.atom4 = a4
        self.atom5 = a5
        self.atom6 = a6

        a1.ring = True
        a2.ring = True
        a3.ring = True
        a4.ring = True
        a5.ring = True

        self.ring_type = 5
        if a6 != None:
            self.ring_type = 6
            a6.ring = True

def find_atom_by_id(checkId):
    """ Given an atom id (such as a1), it will get and return the atom object

    Keyword Arguments:
    checkId -- The id to look for and return the atom
    """
    for i in range(0, len(atom)):
        if atom[i].atom_id == checkId:
            return atom[i]
    else:
        print "no atom found by that id" 

def find_angles(atom, bondList):
    """ Find the angles give an atoms and a list of bonds. Returns a list of angles

    Keyword Arguments:
    atom -- The specific atom to find the angles for
    bondList -- The list of bonds the atom might have
    """
    
    Angles = []
    if atom.Num_Bonds > 1:
       for i in range(0, atom.Num_Bonds):
          ang_type = 1
          if atom.Bonds[0] != atom.Bonds[i]:
              Angles.append(Angle(ang_type,atom.Bonds[0],atom.atom_id,atom.Bonds[i]))
    return Angles

def create_atomobj(atomList):
    """ Create a bunch of atom objects based on the cml file. Returns a list of atom objects

    Keyword Arguments:
    atomList -- The list of atoms found in the cml file to pass in and split
    """
    for i in range(0, len(atomList)):
        atoms.append(help.get_atoms(atomList,i))
        aList = help.object_list(atoms[i])
        atom.append(Atom(aList[0],aList[1],aList[2],aList[3],aList[4]))
    return atom

def create_bondobj(bondList):
    """ Create a bunch of bond objects based on the cml file. Returns a list of bond objects

    Keyword Arguments:
    bondList -- The list of bonds found in the cml file to pass in and split
    """
    for j in range(0, len(bondList)):
        bonds.append(help.get_atoms(bondList,j))
        bList = help.bond_list(bonds[j])
        bond.append(Bond(bList[0],bList[1],bList[2]))
    return bond

def print_atoms(atom):
    """ Prints a list of atoms created by create_atomobj

    Keyword Arguments:
    atom -- The list of atom objects to pass in and print
    """
    print "   ATOMS   "
    print "-----------"
    for k in range(0, len(atom)):
       print "Atom id: %s" % atom[k].atom_id
       print "Atom type: %s" % atom[k].atom_type
       print "X position: %s" % atom[k].x_pos
       print "Y position: %s" % atom[k].y_pos
       print "Z position: %s" % atom[k].z_pos
       print ""

def print_bonds(bond):
    """ Prints a list of bond objects created by create_bondobj

    Keyword Arguments:
    bond -- The list of bond objects to pass in and print
    """
    print "   BONDS   "
    print "-----------"
    for z in range(0, len(bond)):
       print "Bond Number %s" % z
       print "Bond Type: %s" % bond[z].bond_type
       print "Bond Master(bonded from): %s" % bond[z].bond_master
       print "Bond Slave(bonded to): %s" % bond[z].bond_slave
       print ""

def print_find_angles(atom,bond):
    """
    Given a list of atoms and bonds, it finds the angles of the atoms bonded to
    other atoms. It returns a list of angle objects. It also prints the angles without
    needing another statement.

    Keyword Arguments:
    atom -- The list of atom objects to pass in and generate angle objects
    bond -- The list of bond objects to pass in and generate angle objects
    """
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
    return AngleList

def find_dihedrals(AngleList):
    """ Finds the dihedrals given a list of Angle objects. Returns a list of dihedrals

    Keyword Arguments:
    AngleList -- A list of angle objects to calculate the dihedrals from
    """
    dihedrals = []
    for i in range(0,len(AngleList)):
        outerMaster = find_atom_by_id(AngleList[i].Angle_master)
        outerSlave1 = find_atom_by_id(AngleList[i].Angle_slave1)
        outerSlave2 = find_atom_by_id(AngleList[i].Angle_slave2)
        if outerMaster.atom_type == "H" or outerSlave1.atom_type == "H" or outerSlave2.atom_type == "H":
            continue
        outerFirstTwo = [outerMaster,outerSlave1]
        outerFirstTwo.sort()
        for j in range(0,len(AngleList)):
            dihedralObj = []
            if AngleList[j] == AngleList[i]:
                continue
            innerMaster = find_atom_by_id(AngleList[j].Angle_master)
            innerSlave1 = find_atom_by_id(AngleList[j].Angle_slave1)
            innerSlave2 = find_atom_by_id(AngleList[j].Angle_slave2)
            if innerMaster.atom_type == "H" or innerSlave1.atom_type == "H" or innerSlave2.atom_type == "H":
                continue
            innerFirstTwo = [innerMaster,innerSlave1]
            innerSecondTwo = [innerSlave1,innerSlave2]
            innerFirstTwo.sort()
            innerSecondTwo.sort()
            if outerFirstTwo == innerFirstTwo:
                dihedralObj = [outerMaster,outerSlave1,outerSlave2,innerSlave2]
            elif outerFirstTwo == innerSecondTwo:
                dihedralObj = [outerMaster,outerSlave1,outerSlave2,innerMaster]
            else:
                continue
            dihedrals.append(Dihedral(dihedralObj[0],dihedralObj[1],dihedralObj[2],dihedralObj[3]))
    return dihedrals

def print_dihedrals(dihedrals):
    """ Print the atom id's of a list of dihedrals

    Keyword Arguments:
    dihedrals -- the list of dihedrals to print
    """
    for i in range(0,len(dihedrals)):
        print "Dihedral %s: %s" % (i,dihedrals[i])
        print "Dihedral Master1 %s" % (dihedrals[i].Angle_master1.atom_id)
        print "Dihedral Master2 %s" % (dihedrals[i].Angle_master2.atom_id)
        print "Dihedral Slave1 %s" % (dihedrals[i].Angle_slave1.atom_id)
        print "Dihedral Slave2 %s" % (dihedrals[i].Angle_slave2.atom_id)

def find_ring(dihedrals):
    """
    Given a list of dihedrals finds if the dihedrals help to form a ring. It also
    marks the atoms that form a ring. It creates a list of ring objects as well.

    Keyword Arguments:
    dihedrals -- The list of dihedrals to find if rings exist or not
    """
    rings = []
    for i in range(0,len(dihedrals)):
        for j in range(0,len(dihedrals)):
            if dihedrals[i] == dihedrals[j]:
                continue
            if dihedrals[i].Angle_master1.ring == True: 
                continue
            dList = [dihedrals[j].Angle_master1,dihedrals[j].Angle_master2,dihedrals[j].Angle_slave1,dihedrals[j].Angle_slave2]
            outList = [dihedrals[i].Angle_master1,dihedrals[i].Angle_master2,dihedrals[i].Angle_slave1,dihedrals[i].Angle_slave2]
            if dihedrals[i].Angle_master1 not in dList and dihedrals[i].Angle_master2 not in dList:
                if dihedrals[i].Angle_slave1 in dList and dihedrals[i].Angle_slave2 in dList:
                    rings.append(Ring(dihedrals[i].Angle_master1,dihedrals[i].Angle_master2,dihedrals[i].Angle_slave1,dihedrals[i].Angle_slave2,dihedrals[j].Angle_master1,dihedrals[j].Angle_master2))
            elif dihedrals[i].Angle_master1 in dList and dihedrals[i].Angle_slave1 in dList and dihedrals[i].Angle_slave2 in dList:
                if dihedrals[i].Angle_master2 not in dList:
                    rings.append(Ring(dihedrals[i].Angle_master1,dihedrals[i].Angle_master2,dihedrals[i].Angle_slave1,dihedrals[i].Angle_slave2,dihedrals[j].Angle_master2))
            elif dihedrals[i].Angle_master2 in dList and dihedrals[i].Angle_slave1 in dList and dihedrals[i].Angle_slave2 in dList:
                if dihedrals[i].Angle_master1 not in dList:
                    rings.append(Ring(dihedrals[i].Angle_master1,dihedrals[i].Angle_master2,dihedrals[i].Angle_slave1,dihedrals[i].Angle_slave2,dihedrals[j].Angle_master1))
    return rings

def print_ring(rings):
    """ Prints the atom id's from what is contained in the Ring list.

    Keyword Arguments:
    rings -- The list of rings to print and get atom id's from
    """
    for k in range(0,len(rings)):
        print rings[k]
        print rings[k].atom1.atom_id
        print rings[k].atom2.atom_id
        print rings[k].atom3.atom_id
        print rings[k].atom4.atom_id
        print rings[k].atom5.atom_id
        if rings[k].ring_type == 6:
            print rings[k].atom6.atom_id