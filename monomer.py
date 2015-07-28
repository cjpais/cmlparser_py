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
    monomer = Monomer(a,b,an,di,ri,fr)
    return monomer

def mark_thio(monomer):
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
        else:
            continue
