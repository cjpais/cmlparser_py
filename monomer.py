import dihedral
import ring
import sys
import bond

class Monomer(object):
    atoms = []
    bonds = []
    angles = []
    dihedrals = []
    rings = []
    fused_rings = []

    def __init__(self,a,b,an,di,ri,fr):
        self.atoms = a
        self.bonds = b
        self.angles = an
        self.dihedrals = di
        self.rings = ri
        self.fused_rings = fr

def create_monomer(a,b,an,di,ri,fr):
    """ Creates a monomer object with all the data gathered and calculated from
        the input cml file

        Keyword Arguments:
        a - The list of atoms to add to the monomer
        b - The list of bonds to add to the monomer
        an - The list of angles to add to the monomer
        di - The list of dihedrals to add to the monomer
        ri - The list of rings to add to the monomer
        fr - The list of fused rings to add to the monomer
    """
    if len(ri) != 2:
        print "\nWARNING:"
        print "Not valid monomer for cmlparser"
        print "\nQuitting cmlparser. Check that there are exactly 2 rings.\n"
        #quit()
    monomer = Monomer(a,b,an,di,ri,fr)
    return monomer

def mark_thio(monomer):
    """ Mark the thiophene rings in the the monomer by setting the boolean in
        each ring object as well as returning a list of thiophene rings just in
        case they need to be used later.

        Keyword Arguments:
        monomer - The monomer you want to set thiophene rings from. It contains
                  the ring data to set.
    """
    monolist = []
    for i in range(len(monomer.rings)):
        if monomer.rings[i].ring_type == 5:
            mlist = monomer.rings[i].list_type()
            for j in range(4):
                if "C" in mlist:
                    mlist.remove("C")
                else:
                    break
            if "S" in mlist:
                monomer.rings[i].thio = True
                monolist.append(monomer.rings[i])
        else:
            continue
    return monolist

def find_intermono(monomer):
    """ Find the intermonomer dihedral to get a vector from. It just takes a
        single monomer. Right now it just works for the initial one, but theoretically
        it should work for a polymer, just not tested yet.

        Keyword Arguments:
        monomer - The monomer you want to get the intermonomer dihedral
    """
    intermono = ""
    masterbond = ""
    slavebond = ""
    ringlist = monomer.rings[0].list()
    for i in range(len(ringlist)):
        for j in range(len(ringlist[i].atom_bonds)):
            if ringlist[i].atom_bonds[j].ring == True and ringlist[i].atom_bonds[j] not in ringlist:
                masterbond = ringlist[i]
                slavebond = ringlist[i].atom_bonds[j]
    intermono = dihedral.find_dihedral(masterbond,slavebond,monomer.dihedrals)
    return intermono

def get_single_alist(monomer):
    """ Gets a single instance of the monomer to continue to attach. It returns
        a new monomer object with all the relevant data, hopefully.

       Keyword Arguments:
       monomer - The monomer you want to get a single monomer from once you have
                 found the intermonomer dihedral.
    """
    atomlist = monomer.atoms
    bondlist = monomer.bonds
    rings = monomer.rings
    goodring = monomer.rings[len(rings)-2].list()
    badring = monomer.rings[len(rings)-1].list()
    partmono = []
    notgood = []
    checked = []
    for i in range(len(goodring)):
        partmono.append(goodring[i])
        checked.append(goodring[i])
    while len(partmono) != len(atomlist)/len(rings):
        for i in range(len(partmono)):
            for j in range(len(partmono[i].atom_bonds)):
                if partmono[i].atom_bonds[j] in partmono:
                    continue
                if partmono[i].atom_bonds[j] in badring:
                    continue
                else:
                    partmono.append(partmono[i].atom_bonds[j])
    return partmono

def find_attach(polymer,partmono):
    """ Given a monomer/polymer with 2 ends, find which atoms you can attach to. returns
        a list. Which one to add to will be added randomly.

        Keyword Arguments:
        monomer - The monomer/polymer you want to find where to attach the next monomer to
    """
    anglelist = polymer.angles
    for i in range(len(anglelist)):
        if anglelist[i].Angle_master.atom_type == "C" and anglelist[i].Angle_slave1.atom_type == "H" and anglelist[i].Angle_slave2.atom_type == "S" and anglelist[i].Angle_slave1 in partmono:
            print anglelist[i].Angle_slave1.atom_id
            return anglelist[i].Angle_master
        elif anglelist[i].Angle_master.atom_type == "C" and anglelist[i].Angle_slave1.atom_type == "S" and anglelist[i].Angle_slave2.atom_type == "H" and anglelist[i].Angle_slave2 in partmono:
            print anglelist[i].Angle_slave2.atom_id
            return anglelist[i].Angle_master
    print "No valid attachment point found"

def attach(partmono,attach1,monomer,number):
    monomernew = monomer
    while number > 0:
        number -= 1
        attachnew = find_attach(monomernew,partmono)
        attach(partmono,attachnew,monomernew,number)

def create_polymer_cml(filename,partmono,attach,monomer):
    new_cml = open('%s_new.cml' % filename,'w')
    sys.stdout = new_cml
    usedbonds = []
    bondscopy = []
    for i in range(len(monomer.bonds)):
        bondscopy.append(monomer.bonds[i])
    for i in range(len(attach.atom_bonds)):
        if attach.atom_bonds[i].atom_type == "H":
            attach2 = attach.atom_bonds[i]
    abond = bond.get_bond(attach,attach2,monomer.bonds)
    monomer.bonds.remove(abond)
    monomer.atoms.remove(attach2) #find the hydrogen its attached to and remove instead
    add = len(monomer.atoms)+1
    newattach = ""
    anglelist = monomer.angles
    for i in range(len(anglelist)):
        if anglelist[i].Angle_master.atom_type == "C" and anglelist[i].Angle_slave1.atom_type == "C" and anglelist[i].Angle_slave2.atom_type == "S" and anglelist[i].Angle_master in partmono and anglelist[i].Angle_slave1 in partmono and anglelist[i].Angle_slave2 in partmono:
            newattach = anglelist[i].Angle_master
        elif anglelist[i].Angle_master.atom_type == "C" and anglelist[i].Angle_slave1.atom_type == "S" and anglelist[i].Angle_slave2.atom_type == "C" and anglelist[i].Angle_master in partmono and anglelist[i].Angle_slave1 in partmono and anglelist[i].Angle_slave2 in partmono:
            newattach = anglelist[i].Angle_master
    print "<molecule>"
    print " <atomArray>"
    for i in range(len(monomer.atoms)):
        print '  <atom id="a%s" elementType="%s" x3="%s" y3="%s" z3="%s"/>' % (monomer.atoms[i].atom_id,monomer.atoms[i].atom_type,monomer.atoms[i].x_pos,monomer.atoms[i].y_pos,monomer.atoms[i].z_pos)
    for i in range(len(partmono)):
        print '  <atom id="a%s" elementType="%s" x3="%s" y3="%s" z3="%s"/>' % (int(partmono[i].atom_id)+add,partmono[i].atom_type,float(partmono[i].x_pos)-5.00,float(partmono[i].y_pos),float(partmono[i].z_pos))
    print " </atomArray>"
    print " <bondArray>"
    for i in range(len(monomer.bonds)):
        print '  <bond atomRefs2="a%s a%s" order="%s"/>' % (monomer.bonds[i].bond_master.atom_id,monomer.bonds[i].bond_slave.atom_id,monomer.bonds[i].bond_type)
    for i in range(len(partmono)):
        for j in range(len(partmono[i].atom_bonds)):
            if partmono[i].atom_bonds[j] in partmono:
                bondid = bond.get_bond(partmono[i],partmono[i].atom_bonds[j],bondscopy)
                if bondid in usedbonds:
                    continue
                usedbonds.append(bondid)
                print '  <bond atomRefs2="a%s a%s" order="%s"/>' % (int(partmono[i].atom_id)+add,int(partmono[i].atom_bonds[j].atom_id)+add,bondid.bond_type)
            else:
                continue
    print '  <bond atomRefs2="a%s a%s" order="1"/>' % (attach.atom_id,int(newattach.atom_id)+add-2)
    print " </bondArray>"
    print "</molecule>"
    new_cml.close()
