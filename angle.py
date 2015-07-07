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

def set_numbonds(atom,bond):
    numbonds = 0
    bondedTo = []
    for i in range(0,len(bond)):
        if atom.atom_id == bond[i].bond_master.atom_id or atom.atom_id == bond[i].bond_slave.atom_id:
            if atom.atom_id == bond[i].bond_master.atom_id:
                numbonds += 1
                bondedTo.append(bond[i].bond_slave)
            elif atom.atom_id == bond[i].bond_slave.atom_id:
                numbonds += 1
                bondedTo.append(bond[i].bond_master)
    atom.numbonds = numbonds
    atom.atom_bonds = bondedTo

def create_angles(atom,bond):
    angles = []
    for i in range(0,len(atom)):
        set_numbonds(atom[i],bond)
        if atom[i].numbonds > 1:
            for j in range(0,atom[i].numbonds):
                for k in range(j,atom[i].numbonds):
                    atombonds = atom[i].atom_bonds
                    if atombonds[k] != atombonds[j]:
                        angles.append(Angle(1,atom[i],atombonds[j],atombonds[k]))
    return angles
