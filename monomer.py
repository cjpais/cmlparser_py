import dihedral
import ring

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
       inter - The intermonomer dihedral, as not to duplicate code
    """
    atomlist = monomer.atoms
    bondlist = monomer.bonds
    rings = monomer.rings
    goodring = monomer.rings[0].list()
    badring = monomer.rings[1].list()
    partmono = []
    notgood = []
    checked = []
    for i in range(len(goodring)):
        partmono.append(goodring[i])
        checked.append(goodring[i])
    while len(partmono) != len(atomlist)/2:
        for i in range(len(partmono)):
            for j in range(len(partmono[i].atom_bonds)):
                if partmono[i].atom_bonds[j] in partmono:
                    continue
                if partmono[i].atom_bonds[j] in badring:
                    continue
                else:
                    partmono.append(partmono[i].atom_bonds[j])
    print len(partmono)
    for i in range(len(partmono)):
        print "Part of monomer1 %s" % partmono[i].atom_id

def find_attach(monomer):
    """ Given a monomer/polymer with 2 ends, find which atoms you can attach to. returns
        a list. Which one to add to will be added randomly.

        Keyword Arguments:
        monomer - The monomer/polymer you want to find where to attach the next monomer to
    """

    #get a list of rings
    #find which rings have 2 hydrogens attached to them.
    #pick the hydrogen that is correct. This is the hydrogen which is bonded to the carbon bonded to the sulfur.
    #maybe use an angle to find this. The master being a carbon, one slave as a sulfur and the other as hydrogen
