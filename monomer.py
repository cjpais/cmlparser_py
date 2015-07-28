import dihedral

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
        print "Not valid monomer for cmlparser"
        return
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
        The monomer you want to get the intermonomer dihedral
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
