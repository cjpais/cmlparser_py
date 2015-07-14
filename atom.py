class Atom(object):
    atom_id = ""
    atom_type = ""
    x_pos = 0.0000
    y_pos = 0.0000
    z_pos = 0.0000
    numbonds = 0
    atom_bonds = []
    ring = False
    opls_id = 0
    opls_bondid = 0
    opls_partial = 0
    opls_sigma = 0
    opls_epsilon = 0
    opls_mass = 0

    def __init__(self,atom_id,atom_type,x_pos,y_pos,z_pos):
        self.atom_id = atom_id
        self.atom_type = atom_type
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos

def create_atoms(atom):
    atoms = []
    for i in range(0,len(atom)):
        curratom = str(atom[i].attrib).split()
        x = curratom[1].replace(',','').replace("'","")
        y = curratom[3].replace(',','').replace("'","")
        z = curratom[9].replace('}','').replace("'","")
        id = curratom[7].replace('a','').replace(',','').replace("'","")
        type = curratom[5].replace(',','').replace("'","")
        atoms.append(Atom(id,type,x,y,z))
    return atoms
        