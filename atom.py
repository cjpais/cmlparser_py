import os

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
    print_type = 0

    def __init__(self,atom_id,atom_type,x_pos,y_pos,z_pos):
        self.atom_id = atom_id
        self.atom_type = atom_type
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.z_pos = z_pos

def create_atoms(atom):
    """ Creates the atom objects

        Keyword Arguments:
        atom - A list of atom data
    """
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
    """ Gets the unique type of atoms for lammps output

        Keyword Arguments:
        atom - The list of atom objects to get unique types from
    """
    uniq = []
    uniqadd = []
    for i in range(0,len(atom)):
        if atom[i].opls_id in uniqadd:
            continue
        if atom[i].opls_id == 0:
            continue
        uniq.append(atom[i])
        uniqadd.append(atom[i].opls_id)
    return uniq

def periodic_b_size(atom):
    """ Finds a good periodic boundary size for lammps output. Finds min and max
        for x,y,z data from the atoms

        Keyword Arguments:
        atom - The list of atom objects to get x,y,z positional data from.
    """
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
    return float(minx)-10,float(miny)-10,float(minz)-10,float(maxx)+10,float(maxy)+10,float(maxz)+10

def get_type(atom,type):
    """ Gets the type of unique atoms it is for lammps output

        Keyword Arguments:
        atom - The list of atom objects
        type - The list of unique types
    """
    for i in range(len(atom)):
        for j in range(len(type)):
            if atom[i].opls_id == type[j].opls_id:
                atom[i].print_type = j+1
