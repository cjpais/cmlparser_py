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

def uniq_types(atom):
    uniq = []
    uniqadd = []
    for i in range(0,len(atom)):
        if atom[i].opls_id in uniqadd:
            continue
        uniq.append(atom[i])
        uniqadd.append(atom[i].opls_id)
    print uniq
    return uniq

def periodic_b_size(atom):
    minx = 0
    miny = 0
    minz = 0
    maxx = 0
    maxy = 0
    maxz = 0
    for i in range(0,len(atom)):
        if atom[i].x_pos > maxx:
            maxx = atom[i].x_pos
        else:
            minx = atom[i].x_pos
        if atom[i].y_pos > maxy:
            maxy = atom[i].y_pos
        else:
            miny = atom[i].y_pos
        if atom[i].z_pos > maxz:
            maxz = atom[i].z_pos
        else:
            minz = atom[i].z_pos
    return float(minx)-100,float(miny)-100,float(minz)-100,float(maxx)+100,float(maxy)+100,float(maxz)+100