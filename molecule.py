class Molecule(object):
    """docstring for Molecule"""
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

def create_molecule(a,b,an,di,ri,fr):
    molecule = Molecule(a,b,an,di,ri,fr)
    return molecule
