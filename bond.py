class Bond(object):
   bond_type = ""
   bond_equib_len = ""
   bond_force_const = ""
   bond_master = ""
   bond_slave = ""
   opls_bond_num = 0

   #constructor
   def __init__(self, bond_type, bond_master, bond_slave):
      self.bond_type = bond_type
      self.bond_master = bond_master
      self.bond_slave = bond_slave

def create_bonds(bond,atom):
    bonds = []
    for i in range(0,len(bond)):
        currbond = str(bond[i].attrib).split()
        type = currbond[4].replace('}','').replace("'","")
        master = currbond[1].replace('a','').replace(',','').replace("'","")
        slave = currbond[2].replace('a','').replace(',','').replace("'","")
        bonds.append(Bond(type,master,slave))
    change_id_to_atom(bonds,atom)
    return bonds

def change_id_to_atom(bonds,atoms):
    for i in range(0,len(bonds)):
        newbondmaster = bonds[i].bond_master
        newbondslave = bonds[i].bond_slave
        for j in range(0,len(atoms)):
            if atoms[j].atom_id == newbondmaster:
                bonds[i].bond_master = atoms[j]
            if atoms[j].atom_id == newbondslave:
                bonds[i].bond_slave = atoms[j]
