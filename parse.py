import sys
import helper as help

atoms = []
atom = []
bonds = []
bond = []
angle = []
ignore_list = []

#create Atom object
class Atom(object):
    id = ""
    atom_id = ""
    bond_id = ""
    atom_type = ""
    partial_charge = ""
    sigma = ""
    epsilon = ""
    x_pos = 0.000
    y_pos = 0.000
    z_pos = 0.000
    Num_Bonds = 0
    Atom_Bonds = []
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

    #def calc_jones(self):
        #TODO

#create Bond object
class Bond(object):
   bond_type = ""
   bond_equib_len = ""
   bond_force_const = ""
   bond_master = ""
   bond_slave = ""

   #constructor
   def __init__(self, bond_type, bond_master, bond_slave):
      self.bond_type = bond_type
      self.bond_master = bond_master
      self.bond_slave = bond_slave

#create angle object
class Angle(object):
    #Angle_master specifies the master angle. Etc for slaves
    Angle_type = 0
    Angle_equib_len = ""
    Angle_force_const = ""
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
    #these are dihedrals not angles
    dihedral_eqib_len = ""
    dihedral_force_const = ""
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
    improper = False
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

    def list(self):
        rList = []
        rList.append(self.atom1)
        rList.append(self.atom2)
        rList.append(self.atom3)
        rList.append(self.atom4)
        rList.append(self.atom5)
        if self.atom6 != None:
            rList.append(self.atom6)
        return rList

class Fused_Ring(object):
    ring1 = ""
    ring2 = ""

    def __init__(self,ring1,ring2):
        self.ring1 = ring1
        self.ring2 = ring2

class Molecule(object):
    atom_list = ""
    bond_list = ""
    angle_list = ""
    dihedral_list = ""
    ring_list = ""

    def __init__(self,atList,boList,anList,diList,riList):
        self.atom_list = atList
        self.bond_list = boList
        self.angle_list = anList
        self.dihedral_list = diList
        self.ring_list = riList

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
        newBond = Bond(bList[0],bList[1],bList[2])
        bond.append(newBond)
        fromAtom = find_atom_by_id(bList[1])
        toAtom = find_atom_by_id(bList[2])
        fromAtom.Atom_Bonds.append(bList[2])
        toAtom.Atom_Bonds.append(bList[1])
    return bond

def print_atoms(atom, boo = False):
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
       print "Atoms bonded to %s" % atom[k].Atom_Bonds
       print "Number of bonds %s" % atom[k].Num_Bonds
       if boo:
           print "OPLS id %s" % atom[k].id
           print "OPLS bond id %s" % atom[k].bond_id
           print "OPLS sigma %s" % atom[k].sigma
           print "OPLS epsilon %s" % atom[k].epsilon
           print "OPLS partial charge %s" % atom[k].partial_charge
       print ""

def print_bonds(bond,boo = False):
    """ Prints a list of bond objects created by create_bondobj

    Keyword Arguments:
    bond -- The list of bond objects to pass in and print
    """
    print "   BONDS   "
    print "-----------"
    for z in range(0, len(bond)):
       print "Bond Master Type: %s" % find_atom_by_id(bond[z].bond_master).atom_type
       print "Bond Slave Type: %s" % find_atom_by_id(bond[z].bond_slave).atom_type
       print "Bond Number %s" % z
       if boo:
           print "Bond Type: %s" % bond[z].bond_type
           print "Bond Master(bonded from): %s" % bond[z].bond_master
           print "Bond Slave(bonded to): %s" % bond[z].bond_slave
           print "OPLS Force Constant: %s" % bond[z].bond_force_const
           print "OPLS Equilibrium Length: %s" % bond[z].bond_equib_len
       print ""

def print_find_angles(atom,bond):
    """
    Given a list of atoms and bonds, it finds the angles of the atoms bonded to
    other atoms. It returns a list of angle objects.

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
    return AngleList

def print_angles(AngleList,boo = False):
    """
    Given a list of angles, print the angle id's

    Keyword Arguments:
    AngleList -- The list of angles to print
    """
    for x in range(0,len(AngleList)):
        print "Angle Type: %s" % AngleList[x].Angle_type
        print "Master Angle: %s" % AngleList[x].Angle_master
        print "Slave angle 1: %s" % AngleList[x].Angle_slave1
        print "Slave angle 2: %s" % AngleList[x].Angle_slave2
        if boo:
            if find_atom_by_id(AngleList[x].Angle_slave2).bond_id == "":
                print ""
                continue
            print "Master Angle Bond: %s" % find_atom_by_id(AngleList[x].Angle_master).bond_id
            print "Slave Angle Bond: %s" % find_atom_by_id(AngleList[x].Angle_slave1).bond_id
            print "Slave Angle2 Bond: %s" % find_atom_by_id(AngleList[x].Angle_slave2).bond_id
            if AngleList[x].Angle_equib_len == "":
                print "No good data on these bonds"
                print ""
                continue
            print "Equilibrium length %s" % AngleList[x].Angle_equib_len
            print "Force Constant: %s" % AngleList[x].Angle_force_const
        print ""

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

def find_dihedrals_new(AngleList):
    dihedrals = []
    counter = 0
    for i in range(0,len(AngleList)):
        outList = [find_atom_by_id(AngleList[i].Angle_master),find_atom_by_id(AngleList[i].Angle_slave1),find_atom_by_id(AngleList[i].Angle_slave2)]
        if outList[0].atom_type == "H" or outList[1].atom_type == "H" or outList[2].atom_type == "H":
            continue
        for j in range(0,len(AngleList)):
            if AngleList[j] == AngleList[i]:
                continue
            inList = [find_atom_by_id(AngleList[j].Angle_master),find_atom_by_id(AngleList[j].Angle_slave1),find_atom_by_id(AngleList[j].Angle_slave2)]
            inListF = [inList[0],inList[1]]
            inListS = [inList[1],inList[2]]
            if inList[0].atom_type == "H" or inList[1].atom_type == "H" or inList[2].atom_type == "H":
                continue
            if outList[0] in inListF and outList[1] in inListF:
                counter += 1
                print counter
            elif outList[0] in inListS and outList[1] in inListS:
                counter += 1
                print counter
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
    #TODO CLEAN THIS CODE A LOT
    rings = []
    for i in range(0,len(dihedrals)):
        for j in range(0,len(dihedrals)):
            print i
            #if dihedrals[i] == dihedrals[j]:
            #    break
            #if dihedrals[i].Angle_master1.ring == True:
            #    continue
            dList = [dihedrals[j].Angle_master1,dihedrals[j].Angle_master2,dihedrals[j].Angle_slave1,dihedrals[j].Angle_slave2]
            outList = [dihedrals[i].Angle_master1,dihedrals[i].Angle_master2,dihedrals[i].Angle_slave1,dihedrals[i].Angle_slave2]
            if dihedrals[i].Angle_master1 not in dList and dihedrals[i].Angle_master2 not in dList:
                print "out ran"
                print ""
                for k in range(0,len(dList)):
                    #print "dlist %s" % dList[k].atom_id
                    print "outlist %s" % outList[k].atom_id

                if dihedrals[i].Angle_slave1 in dList and dihedrals[i].Angle_slave2 in dList:
                    print "in ran"
                    rings.append(Ring(dihedrals[i].Angle_master1,dihedrals[i].Angle_master2,dihedrals[i].Angle_slave1,dihedrals[i].Angle_slave2,dihedrals[j].Angle_master1,dihedrals[j].Angle_master2))
            elif dihedrals[i].Angle_master1 in dList and dihedrals[i].Angle_slave1 in dList and dihedrals[i].Angle_slave2 in dList:
                if dihedrals[i].Angle_master2 not in dList:
                    rings.append(Ring(dihedrals[i].Angle_master1,dihedrals[i].Angle_master2,dihedrals[i].Angle_slave1,dihedrals[i].Angle_slave2,dihedrals[j].Angle_master2))
            elif dihedrals[i].Angle_master2 in dList and dihedrals[i].Angle_slave1 in dList and dihedrals[i].Angle_slave2 in dList:
                if dihedrals[i].Angle_master1 not in dList:
                    rings.append(Ring(dihedrals[i].Angle_master1,dihedrals[i].Angle_master2,dihedrals[i].Angle_slave1,dihedrals[i].Angle_slave2,dihedrals[j].Angle_master1))
    print rings
    return rings

def find_6ring(dihedrals):
    rings = []
    for i in range(0,len(dihedrals)):
        outList = [dihedrals[i].Angle_master1,dihedrals[i].Angle_master2,dihedrals[i].Angle_slave1,dihedrals[i].Angle_slave2]
        for j in range(0,len(dihedrals)):
            #wtf is going on
            inList = [dihedrals[j].Angle_master1,dihedrals[j].Angle_master2,dihedrals[j].Angle_slave1,dihedrals[j].Angle_slave2]
            print ""
            print "outList"
            for k in range(0,len(outList)):
                print outList[k].atom_id
            print "inList"
            for l in range(0,len(inList)):
                print inList[l].atom_id
    return rings

def remove_duplicates(l):
    """ Given any list remove the duplicates from it

        Keyword Arguments:
        l - Any list that you want to remove duplicates from
    """
    return list(set(l))

def clean_rings(rings):
    """ Removes duplicates of rings to make finding fused rings more accurate

        Keyword Arguments:
        rings - The list of rings to remove duplicates from
    """
    for i in range(0,len(rings)):
        if rings[i].ring_type == 6:
            dup_remove = rings[i].list()
            dup_remove = remove_duplicates(dup_remove)
            rings.remove(rings[i])
            rings.append(Ring(dup_remove[0],dup_remove[1],dup_remove[2],dup_remove[3],dup_remove[4]))
    return rings

def print_ring(rings):
    """ Prints the atom id's from what is contained in the Ring list.

    Keyword Arguments:
    rings -- The list of rings to print and get atom id's from
    """
    print "----------RINGS----------"
    for k in range(0,len(rings)):
        print ""
        print "ring number %d" % k
        print rings[k]
        print rings[k].atom1.atom_id
        print rings[k].atom2.atom_id
        print rings[k].atom3.atom_id
        print rings[k].atom4.atom_id
        print rings[k].atom5.atom_id
        if rings[k].ring_type == 6:
            print rings[k].atom6.atom_id

def find_fused(rings):
    """ Finds which rings are fused given a list of rings. Returns a list of the
        fused rings

        Keyword Arguments:
        rings - The list of rings to check if there are any fused rings
    """
    fused_rings = []
    for i in range(0,len(rings)):
        outRing = rings[i].list()
        for j in range(0,len(rings)):
            inRing = rings[j].list()
            if outRing == inRing:
                continue
            counter = 0
            for k in range(0,len(outRing)):
                for j in range(0,len(inRing)):
                    if outRing[k] == inRing[j]:
                        counter += 1
                        if counter == 2:
                            fused_rings.append(Fused_Ring(inRing,outRing))
                        continue
    return fused_rings

def print_fused(fused):
    """ Prints the fused rings found by the find_fused method. Is void.

        Keyword Arguments:
        fused - The list of fused rings generated by find_fused
    """
    print "----------FUSED RINGS---------"
    for i in range(0,len(fused)):
        print ""
        print fused[i].ring1
        print fused[i].ring2
